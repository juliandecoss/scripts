import boto3
from pprint import pprint
from csv import DictReader
from io import StringIO 
from decimal import Decimal

def get_s3_object(bucket: str, key_path: str) -> dict:
    s3_client = boto3.client(
        's3',
        aws_access_key_id="ASIA3A22TIACE7B3ZO2T",
        aws_secret_access_key="k1t6u6CJvTHI56mkSeY/DVcwBDRQy792o7G8bAD0",
        aws_session_token="IQoJb3JpZ2luX2VjEEAaCXVzLWVhc3QtMSJHMEUCICR0H8o6NKzKpWfZZnCDf/Ra+a9b7M6LVe3IZ0qLnODhAiEA3V17jeSeiZruVUDhYNHAVrc+80sG/DP4nJgbGyybgzAqjAMISRAAGgw3NTc3MTQ4NjIwODQiDIabFH6qgMZcB3gEGirpAo5gU0tU+YZItmt2rwb7qztsjNcVTlBgiZvIG17u+dnADxoNkltGAERWZzcWi/E7VQbmZWTcfMotWsr1n4yE0x0Hg2xJObf7ltOYNsOeKChztCSS3g/mxC73rRVKduL31sOs44mEXTC1ZMuu14v3eJcrYwQ6DXS18nbjTDaddzQvvWrS7KffPww5IcXCk2sfI65O2qkrrZzZw3zz6X4jBsAB5hy9M2FkT2ruUa0wO0ferhpyB0VYuUfOJWdKqfptpQ2kPzIFYjs0/9CvLCKNCCUrSrhPxeIwASQr6hhetSmALh0tsIYApFCYUjPIuW2G4YzQo61eKDKPl9wycj+VtWZW6o7ww7eqAvAf9e4jxrgXngQ3yWfWOSltoKCv4qnAE6fIt9Jt82k5rBOO+Gi7gQ7eR2qstSIMN02yUCZ7IM3E7peScJnrzBbwAZNOj3QS9mr0xCGfqZ4Nkovv+lq5NyzG9vNzzjNh/Qcw4rOqogY6pgF0/Neh1FZU/dq1vWAAb5cVhMGKnTbXLRFbp+rKux5jkRCJmUjqr8QTN2P4VJKKvRvVlmKzKnZpNZ8lmklnLxwn5HR52g1cEH+QysOvNIF0bREWZeP/08SME0EoimJY4AQS0sFSU6AmixNsOwxVMS3RaaNDPl1iWvQ7qV/Ga1cPhlxhAJ5z3b7DGCdXWySIiO5SlvtumQnUw6CG+O10cNmAbDK3beMl",
    )
    response = s3_client.get_object(Bucket=bucket, Key=key_path)
    response["Body"] = response["Body"].read()
    return response

datos = get_s3_object("pf-use1-cost-usage-report-all","757714862084-aws-billing-csv-2023-02.csv")
reader = DictReader(StringIO(datos["Body"].decode()))
bill_information = [row for row in reader]

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

account_cost_allocation = {


    "Data & Data Science": [
        "074242131296", 
        "399968441508", 
        "437993981736", 
        "982396305754"
        ],
    "Finance": [],
    "Financial Services & Ops": [
        "388789109142",
        "526873549260",
        "508311850889",
        "718015228620",
        "353787755460",
        "565787111446",
        "676749124795",
        "323523858898",
        "563241948955", 
        "051790733337",
        "305715501387", 
        "721598394197", 
        "231203291125", 
        "631822849450"
    ],

    "Foundations": [
        "787241336849", 
        "089063602387", 
        "290766746215",
        "337970537845", 
        "366692873704", 
        "454188591425", 
        "555842599842",
        "615034661981", 
        "726101965919", 
        "768090047629", 
        "878689064820",
        "884288795106", 
        "941752626815", 
        "231047417315", 
        "310296967515",
        "572539102928", 
        "740289405046", 
        "757714862084",
        "983478113194", 
        "925696672236", 
        "496308534506"],
    "Fraud Credit Risk & Collections": [
        "925644926633", 
        "639547259187",
        "354773346676",
        "465535879553", 
        "007313948756", 
        "150736303949", 
        "854467266526"
        ],
    "IT Services": [],
    "Payments": [
        "195917654559", 
        "465640780896", 
        "268758445287", 
        "216279324994", 
        "761618848160", 
        "025530844237",
        "796851189729", 
        "845558708917", 
        "859649508664",
        "180979833007", 
        "195917654559", 
        "197377653897", 
        "216279324994",
        "230697266507", 
        "460567525180", 
        "483705751555", 
        "524416272917", 
        "537241170638", 
        "063975098981",
        "065272492515", 
        "108173087725", 
        "731973613410", 
        "645324468339",
        "753291441152", 
        "202374685967", 
        "067868320867", 
        "147561464254"
        ],
    "Other": [
        "673034289294"
    ],


}

product_cost_allocation = {
    "Data & Data Science": [
        "Matillion ETL for Amazon Redshift", 
        "Amazon Athena", 
        "Amazon Managed Workflows for Apache Airflow", 
        "AWS Glue", 
        "AWS Database Migration Service", 
        "AWS Data Pipeline", 
        "Amazon Lex", 
        "Amazon QuickSight", 
        "Amazon SageMaker", 
    ],

    "Finance": [],

    "Financial Services & Ops": [
        "Amazon Connect", 
        "Contact Center Telecommunications (service sold by AMCS, LLC) ", 
        "AWS AppSync", 
        "Amazon CloudFront", 
        "Amazon Pinpoint", 
    ],

    "Fraud Credit Risk & Collections": [],

    "Foundations": [
        # Security
        "Amazon Detective", 
        "AWS Security Hub", 
        "Amazon GuardDuty", 
        "Amazon Cognito", 
        "AWS WAF", 
        "Amazon Macie", 
        "AWS Certificate Manager", 
        "Wazuh Manager 4.0", 
        # Services
        "Apache Kafka® on Confluent Cloud™ - Pay As You Go", 
        "Amazon Route 53", 
        "AWS Key Management Service", 
        "Amazon Virtual Private Cloud", 
        "Amazon Elastic File System", 
        "AWS Secrets Manager", 
        "Amazon Kinesis Firehose", 
        "Amazon DynamoDB", 
        "AWS Backup", 
        "AWS Systems Manager", 
        "AWS CloudTrail", 
        "AWS Cloud Map", 
        "CloudWatch Events", 
        "AWS CodeArtifact", 
        "AWS Service Catalog", 
    ],

    "IT Services": [
        "Amazon WorkSpaces", 
        "AWS Directory Service", 
        "AWS Direct Connect", 
    ],

    "Payments": [],

    "Other": [
        "Fortinet FortiGate Next-Generation Firewall", 
        "Genymotion Cloud : Android 10.0 (Q)", 
        "AWS Data Transfer", 
        "AWS Config", 
        "Amazon Textract", 
        "AWS X-Ray", 
        "AWS CodeCommit", 
        "AWS App Runner", 
        "Amazon Translate", 
        "Amazon Comprehend", 
        "Amazon Registrar", 
        "AWS Amplify", 
        "AWS CodePipeline", 
        "CodeBuild", 
        "AWS Transfer Family", 
        "AWS Global Accelerator", 
        "Amazon DocumentDB (with MongoDB compatibility)", 
        "Amazon Inspector",
    ]
}

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