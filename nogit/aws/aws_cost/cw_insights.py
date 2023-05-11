import boto3
from botocore.client import ClientCreator
from botocore.config import Config
from datetime import datetime
from calendar import monthrange
from typing import Tuple
from typing import Optional
from pytz import timezone
from time import sleep

def get_aws_client(service: str) -> ClientCreator:
    session = boto3.Session(profile_name='david-arana')
    return session.client(service, config=Config(region_name="us-west-2"))


def get_logs_client() -> ClientCreator:
    return get_aws_client("logs")

CW_LOG_GROUP_SSO_API_GW = f'API-Gateway-Execution-Logs_7bmusmlcsh/prod'
CW_LOG_GROUP_CORE_PREFIX = "platform-core" 
DEFAULT_QUERY = """
fields urlRule
| parse urlRule "/*/*" as domain, complement
| parse message "*:*" as label, elapsedtime
| filter ispresent(domain)
| filter message like "time:"
| stats count(*) as request_sum, sum(elapsedtime) as time by concat("/", domain) as domain_url
"""
TODAY = datetime.now()

def get_start_and_end_date(year:int, month:int) -> Tuple[datetime, datetime]:
    start_date = datetime(year, month, 1)
    _ , day_count = monthrange(year,month)
    end_date = datetime(year, month, day_count, 23,59,59)
    return start_date, end_date


def cw_run_query(
    *,
    core_groups: Optional[list] = ["-green","-blue"],
    query: str = DEFAULT_QUERY,
    with_ptr: bool = False,
    start_date: datetime,
    end_date: datetime
) -> list:
    core_groups = core_groups or []
    add_core_prefix = (
        lambda name: CW_LOG_GROUP_CORE_PREFIX + name if name else ""
    )
    log_groups = [add_core_prefix(core_group) for core_group in core_groups]
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
