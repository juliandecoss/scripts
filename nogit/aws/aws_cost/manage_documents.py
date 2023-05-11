from os import path, mkdir,getcwd
import sys
import boto3
import botocore
from csv import writer
from cw_insights import cw_run_query, parse_cw_results, get_start_and_end_date
from new_relic_queries import run_query_by_graphql

# pip3 install boto3, pytz, requests, graphql-query

##################################################
# Get Arguments
##################################################
month = sys.argv[1]
year = sys.argv[2]

##################################################
# Create directory
##################################################

par = getcwd()
parent_dir = par +f"/src/{year}"
if not path.isdir(parent_dir):
    directory = mkdir(parent_dir)
directory_path = path.join(parent_dir, month)
if not path.isdir(directory_path):
    directory = mkdir(directory_path)
    print("Directory '% s' created" % directory)
else:
    print("the directory is already created")


##################################################
# Download bill.csv
##################################################

if not path.isfile(directory_path+"/bill.csv"):
    month_for_bucket = "0"+month if int(month)<10 else month
    BUCKET_NAME = 'pf-use1-cost-usage-report-all' # replace with your bucket name
    KEY = f"757714862084-aws-billing-csv-{year}-{month_for_bucket}.csv" # replace with your object key
    session = boto3.Session(profile_name='organization-management')
    s3 = session.resource('s3')

    try:
        s3.Bucket(BUCKET_NAME).download_file(KEY, directory_path+"/bill.csv")
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise
    print(f"the file bill.csv has been created in {directory_path}")
else:
    print("the file bill.csv already exists")

##################################################
# Create core insights.csv
##################################################

if not path.isfile(directory_path+"/insights.csv"):
    start_date, end_date = get_start_and_end_date(int(year),int(month))
    core_routes = cw_run_query(start_date=start_date, end_date=end_date)
    insights_information = parse_cw_results(core_routes)

    with open(directory_path+"/insights.csv", "w") as insights_file:
        insights_writer = writer(insights_file, delimiter=",")
        insights_writer.writerow(
                ['Domain_url', 'Request_sum', 'Time']
            )
        for info in insights_information:
            insights_writer.writerow([info['domain_url'],info['request_sum'], info['time']])
    print(f"the file insights.csv has been created in {directory_path}")
else:
    print("the file insights.csv already exists")

##################################################
# Create lambda.csv
##################################################
if not path.isfile(directory_path+"/lambda.csv"):
    LAMBDA_QUERY = "SELECT (sum(`aws.lambda.Duration.byFunction`) / 1000) as 'Duration' FROM Metric FACET `tags.squad` as 'Squads', aws.lambda.memorySize as 'Memory' SINCE last month until this month limit max"
    lambda_data = run_query_by_graphql(LAMBDA_QUERY)
    with open(directory_path+"/lambda.csv", "w") as lambda_file:
        lambda_writer = writer(lambda_file, delimiter=",")
        lambda_writer.writerow(
                ['Squads', 'Memory', 'Duration']
            )
        for info in lambda_data:
            squad=info['facet'][0]
            memory=info['facet'][1]
            lambda_writer.writerow([squad,memory, info['Duration']])
    print(f"the file lambda.csv has been created in {directory_path}")
else:
    print("the file lambda.csv already exists")

##################################################
# Create rds.csv
##################################################
if not path.isfile(directory_path+"/rds.csv"):
    RDS_QUERY = "SELECT sum(apm.service.datastore.operation.duration) as 'Database operation Duration', count(apm.service.datastore.operation.duration) as 'Database operation Calls' FROM Metric WHERE (entity.guid = 'MzU3NzYxMnxBUE18QVBQTElDQVRJT058MTA0NjUzNDU5OA') AND ((operation is not NULL AND datastoreType = 'MySQL')) FACET `scope` LIMIT max since last month UNTIL this month"
    rds_data = run_query_by_graphql(RDS_QUERY)
    with open(directory_path+"/rds.csv", "w") as rds_file:
        rds_writer = writer(rds_file, delimiter=",")
        rds_writer.writerow(
                ['Scope', 'Database operation Duration', 'Database operation Calls']
            )
        for info in rds_data:
            rds_writer.writerow([info['facet'], info['Database operation Duration'], info['Database operation Calls']])
        print(f"the file rds.csv has been created in {directory_path}")
else:
    print("the file rds.csv already exists")

##################################################
# Create redshift.csv
##################################################
if not path.isfile(directory_path+"/redshift.csv"):
    REDSHIFT_QUERY = "SELECT count(apm.service.datastore.operation.duration) as 'Database operation Duration', sum(apm.service.datastore.operation.duration) as 'Database operation Calls' FROM Metric WHERE (entity.guid = 'MzU3NzYxMnxBUE18QVBQTElDQVRJT058MTA0NjUzNDU5OA') AND ((operation is not NULL AND datastoreType = 'Postgres')) FACET `scope` LIMIT max since last month UNTIL this month"
    redshift_data = run_query_by_graphql(REDSHIFT_QUERY)
    with open(directory_path+"/redshift.csv", "w") as redshift_file:
        redshift_writer = writer(redshift_file, delimiter=",")
        redshift_writer.writerow(
                ['Scope', 'Database operation Duration', 'Database operation Calls']
            )
        for info in redshift_data:
            redshift_writer.writerow([info['facet'], info['Database operation Duration'], info['Database operation Calls']])
else:
    print("the file rds.csv already exists")
