from time import sleep
from typing import Optional

from pytz import timezone
from datetime import datetime, timedelta
from typing import Tuple
from botocore.client import ClientCreator
from botocore.config import Config
from boto3 import client

TODAY = datetime.now()
CW_LOG_GROUP_SSO_API_GW = f'API-Gateway-Execution-Logs_7bmusmlcsh/prod'
DEFAULT_QUERY = "fields timestamp, email"
CW_LOG_GROUP_SSO_LAMBDA_PREFIX = "/aws/lambda/sso-"
CW_LOG_GROUP_SSO_FORGOT_PASSWORD = "forgot-password"

SUCCESS_RATE_FORGOT_PASSWORD = """
filter stage = 'prod' and statusCode = 200
| stats sum(message='Confirmation code successfully sent') as email_sent,
        sum(message='Credential successfully reset') as password_reset
"""

def get_start_and_end_date() -> Tuple[datetime, datetime]:
    last_friday = TODAY - timedelta(days=7)
    start_date = datetime(last_friday.year, last_friday.month, last_friday.day,last_friday.hour,last_friday.minute)
    end_date = datetime(
        TODAY.year, TODAY.month, TODAY.day, TODAY.hour, TODAY.minute
    )
    return start_date, end_date

def get_aws_client(service: str) -> ClientCreator:
    return client(service, config=Config(region_name='us-west-2'))


def get_logs_client() -> ClientCreator:
    return get_aws_client("logs")

def cw_run_query(
    *,
    lambda_group: str = "",
    lambda_groups: Optional[list] = None,
    on_api_group: bool = False,
    query: str = DEFAULT_QUERY,
    with_ptr: bool = False,
) -> list:
    lambda_groups = lambda_groups or []
    add_lambda_prefix = (
        lambda name: CW_LOG_GROUP_SSO_LAMBDA_PREFIX + name if name else ""
    )
    log_groups = [add_lambda_prefix(lambda_group) for lambda_group in lambda_groups]
    if not log_groups:
        log_groups.append(add_lambda_prefix(lambda_group) or CW_LOG_GROUP_SSO_API_GW)
    if on_api_group and not CW_LOG_GROUP_SSO_API_GW in log_groups:
        log_groups.append(CW_LOG_GROUP_SSO_API_GW)
    start_date, end_date = get_start_and_end_date()
    time_zone = timezone("America/Mexico_City")
    start_timestamp = int(start_date.astimezone(time_zone).timestamp())
    end_timestamp = int(end_date.astimezone(time_zone).timestamp())
    sleep_time = (end_timestamp - start_timestamp) // (
        (end_timestamp - start_timestamp) // 2
    ) or 1
    cw = get_logs_client()
    cw_query = cw.start_query(
        logGroupNames=log_groups,
        startTime=start_timestamp,
        endTime=end_timestamp,
        queryString=query,
    )
    query_id = cw_query["queryId"]
    get_query_results = cw.get_query_results
    query_results_params = {"queryId": query_id}
    cw_result = get_query_results(**query_results_params)
    while cw_result["status"] in ["Running", "Scheduled"]:
        sleep(sleep_time)
        print("de dormir ando chambeando")
        cw_result = get_query_results(**query_results_params)
    if cw_result["status"] != "Complete":
        raise Exception("There was a cw query problem")
    results = cw_result["results"]
    if not with_ptr:
        for log_event in results:
            for idx, obj in enumerate(log_event):
                if obj["field"] == "@ptr":
                    log_event.pop(idx)
    return results


def parse_cw_results(results: list) -> list:
    log_events = []
    for log_event in results:
        log = {obj["field"]: obj["value"] for obj in log_event}
        if log:
            log_events.append(log)
    return log_events


def get_forgot_password_success_rate() -> str:
    results = cw_run_query(lambda_group=CW_LOG_GROUP_SSO_FORGOT_PASSWORD, query=SUCCESS_RATE_FORGOT_PASSWORD)
    logs = parse_cw_results(results)
    success_rate = int(logs[0]['password_reset'])/int(logs[0]['email_sent'])
    return format(success_rate, ".2%")

sr = get_forgot_password_success_rate()
print(sr)