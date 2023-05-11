import boto3
from pprint import pprint
from csv import DictReader
from io import StringIO 
from decimal import Decimal
from constants import product_cost_allocation, account_cost_allocation, tribe_domains, structure, core_related_services
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
import json
from pprint import pprint

import requests
from graphql_query import Argument, Field, Operation, Query

def get_s3_object(bucket: str, key_path: str) -> dict:
    s3_client = boto3.client(
        's3',
        aws_access_key_id="ASIA3A22TIACGIQRXRGQ",
        aws_secret_access_key="76itmWHwG4IeDLq+v27zTaUhNL503BlqFitVDr2f",
        aws_session_token="IQoJb3JpZ2luX2VjEFgaCXVzLWVhc3QtMSJHMEUCIQDqWdOW9wjYW7LBlQIgLTrkKt/hkFeY8wbQcR2kxSg+zQIgbmMJnZggsHvA4W0oirhcVD/RoTOLFZCKSBwbfsOMG7sqjAMIYRAAGgw3NTc3MTQ4NjIwODQiDNji6OZN+gFjRDEtYCrpAlLSrwuWoO5zRn5gUsMemsqMXn/das42A7Ok9WUHEs+KyZywrfrCk7QMDE/Yc7d67GMfMLKB8ovbTAycnMat+pWcciMBtet0UWFInP8RzcN2luQS2l4qBJ8Z5uuJ1UH7wD9mT0dcdUrJdI6b/S5CLW6thLIvfq8eHRUjYQz2rwylcXa0atsqpDJ1+xftkAD2Z9dFY4cd4lQ8qpZzINU73o/mQWRhfV1DNMhre6/Y5L3/MA7E+owYfSDIW2u4c8PtN95O8lRti+p15AiYYliRj8yRIoJTnOkUtPCkaEg0kzOK+Z9K4U0dhZxOUXSPxu94MJf4kK0o/mh1u8yv/okK+JH/F5WO0GVpX3Prk+lXfU8+tM13zjuJ+YqRwCRCQLxN2HZ2hgxktEKTTqujPXoRiiwM9VsTYxw21ofvDfCRhEenT8cVZvFLsY/17dOdbegdDCYikXshtBvYzd1vwn8BbbJtBwXPWcKo09sw7cyvogY6pgE2g05UuqFSA/N4S99/I1lEd0WFg+5j0C3ahMvPL3C2m7DKE9ZLotIVcYy9v69vVye4AU+3AGKjrVucEMr6iDMBEHnOHCRNzig1M2O9yIKvzIemojZODtBjhwjbV3uZ597RUAmz5YXFZQoCFh/ovCGO2bJg8ETvuZESEGU2er1hhsXn1qELhTM9Z9WXRpdHeW2SG51TktwLNVSGMFU9KMMohkk2L+jH",
    )
    response = s3_client.get_object(Bucket=bucket, Key=key_path)
    response["Body"] = response["Body"].read()
    return response

datos = get_s3_object("pf-use1-cost-usage-report-all","757714862084-aws-billing-csv-2023-02.csv")
reader = DictReader(StringIO(datos["Body"].decode()))
bill_information = [row for row in reader]


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


##################################################
# Script de costos
##################################################
total = 0

for row in bill_information:
    record_type = row.get("RecordType")
    if record_type == "AccountTotal":
        total += round(Decimal(row.get("CostBeforeTax", 0)), 2)

debug = True
def dprint(*m, force=False):
    if debug or force:
        print(*m)
        
dprint("# =========================================")
dprint("# Total:", total)
dprint("# =========================================")
dprint("")

cost_allocation_by_account = {}
allocated_rows = []
unknown_accounts = {}
for tribe in list(account_cost_allocation.keys()):
    tribe_accounts = account_cost_allocation[tribe]
    for row_number in range(len(bill_information)):
        row = bill_information[row_number]
        account_id = row.get("LinkedAccountId", "") or row.get("PayerAccountId", "")
        record_type = row.get("RecordType")
        if account_id in tribe_accounts:
            if record_type == "AccountTotal":
                cost_allocation_by_account[tribe] = cost_allocation_by_account.get(tribe) or 0
                cost_allocation_by_account[tribe] += round(Decimal(row.get("CostBeforeTax", 0)), 2)
                allocated_rows.append(row_number)
cost_allocation_by_account["Foundations"] -= 18600
bill_information = [bill_information[row_number] for row_number in range(len(bill_information)) if row_number not in allocated_rows]
def sum_cost(cost_result):
    total = 0
    for k in list(cost_result.keys()):
        total += Decimal(cost_result[k])
    return total

##################################################
# Groups costs by product
##################################################

products_cost = {}
for row in bill_information:
    product = row.get("ProductName", "")
    account = row.get("LinkedAccountId", "")
    if account == "180477243137":
        if not product:
            continue
        products_cost[product] = products_cost.get(product, 0) or  0
        products_cost[product] += round(Decimal(row.get("CostBeforeTax", 0)), 2)


##################################################
# Allocate costs by product
##################################################

cost_allocation_by_product = {}
for tribe in list(product_cost_allocation.keys()):
    tribe_products = product_cost_allocation[tribe]
    for product in list(products_cost.keys()):
        if product in tribe_products:
            cost_allocation_by_product[tribe] = cost_allocation_by_product.get(tribe) or 0
            cost_allocation_by_product[tribe] += round(Decimal(products_cost[product]), 2)
            del products_cost[product]

dprint("# =========================")
dprint("# Cost allocation by ACCOUNT")
dprint("#  - Total:", sum_cost(cost_allocation_by_account))
dprint(cost_allocation_by_account)
dprint("# =========================")
dprint("# Cost allocation by PRODUCT")
dprint("#  - Total:", sum_cost(cost_allocation_by_product))
dprint(cost_allocation_by_product)
dprint("# =========================")

##########################################################
# Core Consumption: Weight: (time * 0.7) + (count * 0.3)
##########################################################

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


core_routes = cw_run_query()
insights_information = parse_cw_results(core_routes)
distribution_by_qty, distribution_by_time = get_cost_distribution(insights_information, "core")
total_weighted, weighted_consumption_core = get_weighted_cost(distribution_by_qty, distribution_by_time)

# total_assigned_to_core = 0
# for product in list(products_cost.keys()):
#     if product in core_related_services:
#         total_assigned_to_core += products_cost[product]
#         del products_cost[product]

# for tribe in list(weighted_consumption_core.keys()):
#     weighted_consumption_core[tribe] = round(total_assigned_to_core * weighted_consumption_core[tribe], 2)

# dprint("# =========================")
# dprint("# Cost allocation by CORE USAGE")
# dprint("# - Total:", total_assigned_to_core)
# dprint(weighted_consumption_core)
# dprint("# =========================")

##################################################
# RDS Distribution: Same weight
##################################################

KEY = "NRAK-8NPHBEN3SKA9T9EJZHUDRALQT1U"
query = "SELECT count(apm.service.datastore.operation.duration) as 'Database operation Duration', sum(apm.service.datastore.operation.duration) as 'Database operation Calls' FROM Metric WHERE (entity.guid = 'MzU3NzYxMnxBUE18QVBQTElDQVRJT058MTA0NjUzNDU5OA') AND ((operation is not NULL AND datastoreType = 'Postgres')) FACET `scope` LIMIT max since last month UNTIL this month"
actor = Query(
    name="actor",
    fields=[
        Field(
            name="account",
            arguments=[Argument(name="id", value=3577612)],
            fields=[
                Field(
                    name="nrql",
                    arguments=[Argument(name="query", value=f'"{query}"')],
                    fields=["results"],
                )
            ],
        )
    ],
)
hero = Query(
    name="account",
    arguments=[Argument(name="id", value=3577612)],
    fields=[
        Field(
            name="nrql",
            arguments=[Argument(name="query", value=f'"{query}"')],
            fields=["results"],
        )
    ],
)
operation = Operation(type="", queries=[actor])
endpoint = "https://api.newrelic.com/graphql"
headers = {"API-Key": f"{KEY}"}
response = requests.post(endpoint, headers=headers, json={"query": operation.render()})

if response.status_code == 200:
    json_dictionary = json.loads(response.content)
    rds_information = json_dictionary["data"]["actor"]["account"]["nrql"]["results"]
new_rds_info = []
for info in rds_information:
    info['Scope'] = info.pop('scope')
    new_rds_info.append(info)
rds_information = new_rds_info

consumption_by_qty, consumption_by_time = get_cost_distribution(rds_information, "rds")
total_weighted, weighted_consumption_rds = get_weighted_cost(consumption_by_qty, consumption_by_time)

total_assigned_to_rds = products_cost["Amazon Relational Database Service"]

for tribe in list(weighted_consumption_rds.keys()):
    weighted_consumption_rds[tribe] = round(total_assigned_to_rds * weighted_consumption_rds[tribe], 2)

del products_cost["Amazon Relational Database Service"]
dprint("# =========================")
dprint("# Cost allocation by RDS USAGE")
dprint("# - Total:", total_assigned_to_rds)
dprint(weighted_consumption_rds)
dprint("# =========================")

##################################################
# Redshift Distribution: Same weight
##################################################

consumption_by_qty, consumption_by_time = get_cost_distribution(rds_information, "redshift")
total_weighted, weighted_consumption_redshift = get_weighted_cost(consumption_by_qty, consumption_by_time)

total_assigned_to_redshift = products_cost["Amazon Redshift"]

for tribe in list(weighted_consumption_redshift.keys()):
    weighted_consumption_redshift[tribe] = round(total_assigned_to_redshift * weighted_consumption_redshift[tribe], 2)

del products_cost["Amazon Redshift"]