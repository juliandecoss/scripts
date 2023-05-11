from time import sleep
from typing import Optional

from pytz import timezone
from os import environ

from boto3 import client
from botocore.client import ClientCreator
from botocore.config import Config
from datetime import datetime, timedelta
from typing import Tuple
from decimal import Decimal


def get_aws_client(service: str) -> ClientCreator:
    return client(service, config=Config(region_name="us-west-2"))


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
def get_start_and_end_date() -> Tuple[datetime, datetime]:
    last_friday = TODAY - timedelta(days=1,weeks=12)
    start_date = datetime(
        last_friday.year,
        last_friday.month,
        last_friday.day,
        0,
    )
    today = last_friday + timedelta(days=27)
    end_date = datetime(today.year, today.month, today.day, 23, 59, 59)
    return start_date, end_date


def cw_run_query(
    *,
    core_groups: Optional[list] = ["-green","-blue"],
    query: str = DEFAULT_QUERY,
    with_ptr: bool = False,
) -> list:
    core_groups = core_groups or []
    add_core_prefix = (
        lambda name: CW_LOG_GROUP_CORE_PREFIX + name if name else ""
    )
    log_groups = [add_core_prefix(core_group) for core_group in core_groups]
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


core_routes = cw_run_query()
insights_information = parse_cw_results(core_routes)
from pprint import pprint
pprint(insights_information)
breakpoint()

##########################################################
# Core Consumption: Weight: (time * 0.7) + (count * 0.3)
##########################################################
tribe_domains = {
    
    "Data & Data Science": [
        "ab-testing",
    ],

    "Finance": [
        "finance",
        "transactions",
        "capital-markets",
        "maker",
    ],

    "Financial Services & Ops": [
        "loans",
        "gmodelo", # no hits during september
        "partners",
        "secured",
        "funnel",
        "bundle",
        "kts",
        "cards",
        "benefits",
        "product",
        "growth",
        "dynamic-stages",
        "account-creation",
        "client",
        "mgm",
        "entities",
        "enterprise",
        "people",
        "assignment",
        "servicing",
        "verification",
        "documents",
        "docs",
        "support",
        "compliance",
        "mifiel",
        "reporting",
        "notifications",   
    ],

    "Foundations": [
        "sso",
        "auth",
        "identity",
        "integration",
    ],

    "Fraud Credit Risk & Collections": [
        "scoring",
        "scraping",
        "mining",
        "comms",
        "decision-tree",
        "phones", # no hits during september
        "phone",
        "collections",
        "services",
    ],

    "IT Services": [],

    "Payments": [
        "payments",
        "konfio-pay",
        "erp",
        "subscriptions",
        "shop",
        "logistic",
    ],

    "Other": [
        "kompas",
        "insurance",
    ]
}


structure = {
    "core": {
        "domain": "domain_url",
        "count": "request_sum",
        "time": "time",
    },
    "rds": {
        "domain": "Scope",
        "count": "Database operation Calls",
        "time": "Database operation Duration",
    },
    "redshift": {
        "domain": "Scope",
        "count": "Database operation Calls",
        "time": "Database operation Duration",
    }
}

def get_weighted_cost(consumption_by_qty, consumption_by_time):

    weighted_consumption = {}
    for tribe in list(consumption_by_qty.keys()):
        pct_qty = Decimal(0.7) * Decimal(consumption_by_qty[tribe])
        pct_time = Decimal(0.3) * Decimal(consumption_by_time[tribe])
        weighted_consumption[tribe] = round(pct_qty + pct_time, 2)

    total_weighted = 0
    for tribe in list(weighted_consumption.keys()):
        total_weighted += weighted_consumption[tribe]

    first_tribe = list(weighted_consumption.keys())[0]
    if 1 - total_weighted > 0:
        weighted_consumption[first_tribe] += 1 - total_weighted
    elif weighted_consumption[first_tribe] - (1 - total_weighted) > 0: 
        weighted_consumption[first_tribe] -= (1 - total_weighted)

    total_weighted = 0
    for tribe in list(weighted_consumption.keys()):
        total_weighted += weighted_consumption[tribe]

    return total_weighted, weighted_consumption

def get_cost_distribution(information, category): 

    total_by_qty = 0
    total_by_time = 0
    consumption_by_qty = {}
    consumption_by_time = {}

    dict_keys = structure.get(category, {})

    for domain in information:
        total_by_qty += int(domain.get(dict_keys.get("count"), 0))
        total_by_time += round(Decimal(domain.get(dict_keys.get("time"), 0)), 2)
        for tribe in list(tribe_domains.keys()):
            if clean_domain(domain.get(dict_keys.get("domain"))) in tribe_domains[tribe]:
                consumption_by_qty[tribe] = consumption_by_qty.get(tribe, 0)
                consumption_by_time[tribe] = consumption_by_time.get(tribe, 0)
                consumption_by_qty[tribe] += int(domain.get(dict_keys.get("count"), 0))
                consumption_by_time[tribe] += round(Decimal(domain.get(dict_keys.get("time"), 0)), 2)

    distribution_by_qty = {}
    distribution_by_time = {}
    for tribe in list(consumption_by_qty.keys()):
        distribution_by_qty[tribe] = round(consumption_by_qty[tribe] / total_by_qty, 4)
        distribution_by_time[tribe] = round(consumption_by_time[tribe] / total_by_time, 4)

    return distribution_by_qty, distribution_by_time


def clean_domain(domain):
    clean_domain = domain.replace("WebTransaction/Function/core.routes.", "")
    clean_domain = clean_domain.split(".")[0]
    clean_domain = clean_domain.replace("/", "")
    return clean_domain

distribution_by_qty, distribution_by_time = get_cost_distribution(insights_information, "core")
total_weighted, weighted_consumption_core = get_weighted_cost(distribution_by_qty, distribution_by_time)

# total_assigned_to_core = 0
# for product in list(products_cost.keys()):
#     if product in core_related_services:
#         total_assigned_to_core += products_cost[product]
#         del products_cost[product]

# for tribe in list(weighted_consumption_core.keys()):
#     weighted_consumption_core[tribe] = round(total_assigned_to_core * weighted_consumption_core[tribe], 2)