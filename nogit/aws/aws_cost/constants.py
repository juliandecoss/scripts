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

core_related_services = [
    "Amazon Elastic Compute Cloud", 
    "Amazon Elastic Container Service", 
    "Elastic Load Balancing", 
    "Amazon ElastiCache", 
    "Amazon OpenSearch Service", 
    "Amazon API Gateway", 
    "Amazon Elastic Container Registry Public", 
    "Amazon Elastic Container Service for Kubernetes", 
    "AWS Step Functions", 
    "Amazon Simple Email Service", 
    "Amazon EC2 Container Registry (ECR)", 
]