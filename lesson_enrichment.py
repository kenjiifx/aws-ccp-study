"""Extra teaching content per lesson: exam traps, service comparisons, additional points."""

LESSON_ENRICH = {
    "1.1": {
        "extra_points": [
            "🔄 High availability (HA) = stay online when something breaks. Elasticity = grow and shrink with traffic. The exam tests both — don't mix them up!",
            "🌐 Fault tolerance = the system keeps working even when parts fail. You get this by spreading across multiple Availability Zones.",
            "📍 Stop guessing capacity — in the old days you bought servers for your busiest day and they sat idle. Cloud lets you pay only for what you use today.",
            "🏃 Go global in minutes — launch in Tokyo, London, or São Paulo without building a data center there first.",
            "🆓 AWS Free Tier gives limited free usage for 12 months (and some always-free services) — great for learning, not unlimited production forever.",
        ],
        "comparisons": [
            {"title": "Elasticity vs Agility", "text": "Elasticity is like adding more chairs when more guests arrive. Agility is like trying a new recipe tonight without buying a whole new kitchen."},
            {"title": "Public vs Private vs Hybrid cloud", "text": "Public = AWS shared cloud. Private = your own servers only. Hybrid = some at home, some in AWS (very common when migrating)."},
            {"title": "High availability vs Fault tolerance", "text": "Both help you stay online. HA focuses on minimal downtime. Fault tolerance means one broken part does not kill the whole app."},
            {"title": "Scalability vs Elasticity", "text": "Scalability means the system CAN grow. Elasticity means it grows and shrinks automatically without manual work."},
        ],
        "traps": [
            "⚠️ EXAM TRAP: 'Pay for unused resources' is NOT a cloud benefit — the opposite is true! You scale down to stop paying.",
            "⚠️ EXAM TRAP: Edge locations are NOT the same as Regions. Regions hold your servers. Edge locations cache content closer to users (CloudFront).",
            "⚠️ EXAM TRAP: Community cloud is rare on the exam. If they ask about AWS, answer is almost always public cloud.",
            "⚠️ EXAM TRAP: Durability (data won't be lost) is not the same as elasticity (auto scale). S3 is durable; EC2 autoscaling is elastic.",
        ],
    },
    "1.2": {
        "extra_points": [
            "🌱 Sustainability pillar = use only the cloud power you need. Fewer idle servers means less wasted energy.",
            "📋 Well-Architected is NOT a service you turn on — it is a set of best-practice questions AWS recommends for every workload.",
            "🔁 Operational Excellence also means learning from failures and improving runbooks, not just keeping the lights on.",
            "🧪 Use the Well-Architected Tool in the console to run a free review and get improvement suggestions per pillar.",
            "📐 Design for failure — assume things will break and build so one failure does not take down everything (Reliability pillar).",
        ],
        "comparisons": [
            {"title": "Security vs Reliability", "text": "Security stops bad guys and protects data. Reliability keeps the app running when hardware fails."},
            {"title": "Performance Efficiency vs Cost Optimization", "text": "Performance = right tool for speed. Cost = right tool for price. A tiny instance can be cheap but too slow — balance both pillars."},
            {"title": "All six pillars", "text": "Operations, Security, Reliability, Performance, Cost, Sustainability — know one real-world example for each."},
            {"title": "Well-Architected vs CAF", "text": "Well-Architected = how to design a good workload. CAF = how to adopt cloud across your whole organization."},
        ],
        "traps": [
            "⚠️ EXAM TRAP: Rightsizing is Cost Optimization, not Performance Efficiency (though they overlap).",
            "⚠️ EXAM TRAP: Multiple AZs = Reliability pillar, not Cost Optimization.",
            "⚠️ EXAM TRAP: There are exactly SIX pillars. Sustainability was added — older guides sometimes list five.",
            "⚠️ EXAM TRAP: Encryption is Security pillar, not Operational Excellence — even though ops teams enable it.",
        ],
    },
    "1.3": {
        "extra_points": [
            "♻️ Retire = shut down apps you no longer need. Retain = keep some workloads on-premises on purpose.",
            "🛒 Repurchase = move to SaaS (like Salesforce) instead of running the app yourself on EC2.",
            "📡 Application Migration Service (MGN) and Server Migration Service help move servers to AWS.",
            "📖 AWS Prescriptive Guidance = free step-by-step migration guides on the AWS website.",
            "❄️ Snowmobile (Snowmobile truck) moves exabytes — Snowball Edge can run compute at the edge during transfer.",
        ],
        "comparisons": [
            {"title": "Snowball vs DataSync vs Direct Connect", "text": "Snowball = ship a physical box of data (huge one-time move). DataSync = automated online sync over the network. Direct Connect = private pipe between your office and AWS."},
            {"title": "DMS vs SCT", "text": "DMS copies data while the database keeps running. SCT converts the database schema when changing engines (Oracle → PostgreSQL)."},
            {"title": "Rehost vs Replatform vs Refactor", "text": "Rehost = lift-and-shift unchanged. Replatform = small tweaks (e.g. move to RDS). Refactor = rewrite for cloud-native (Lambda, microservices)."},
            {"title": "Migration Hub vs MGN", "text": "Migration Hub tracks and organizes migration progress across tools. MGN actually replicates and cut over servers."},
        ],
        "traps": [
            "⚠️ EXAM TRAP: Snowball is for OFFLINE bulk transfer, not day-to-day database replication — that is DMS.",
            "⚠️ EXAM TRAP: CAF is about adoption strategy, not the Well-Architected Framework (that is for designing workloads).",
            "⚠️ EXAM TRAP: Migration Hub tracks progress — it does not physically move data.",
            "⚠️ EXAM TRAP: Replatform is NOT the same as refactor. Replatform = small changes; refactor = major rewrite for cloud.",
        ],
    },
    "1.4": {
        "extra_points": [
            "🔌 On-premises hidden costs: building rent, power, cooling, hardware repairs, and IT staff to rack servers.",
            "📊 Variable cost = your bill goes up when you use more and down when you use less, like a water meter.",
            "🏷️ Included licenses = AWS bundles software cost in the price (common on managed services). BYOL = you bring licenses you already own.",
            "⏱️ Time to market — cloud removes months of hardware procurement so you launch products faster (agility + economics).",
            "📉 Underutilization on-premises means you paid for servers that sit idle most of the year — cloud fixes that.",
        ],
        "comparisons": [
            {"title": "CapEx vs OpEx", "text": "CapEx = big upfront purchase (buying servers). OpEx = monthly pay-as-you-go (AWS bill). Cloud shifts CapEx to OpEx."},
            {"title": "Rightsizing vs Autoscaling", "text": "Rightsizing = pick the correct instance size. Autoscaling = change HOW MANY instances run. Both save money."},
            {"title": "BYOL vs included license", "text": "BYOL needs Dedicated Hosts or special agreements. Included license = simpler, AWS handles licensing on managed services."},
            {"title": "Fixed vs variable cost", "text": "On-premises = mostly fixed (you own the server whether you use it or not). Cloud = mostly variable (pay per hour/GB/request)."},
        ],
        "traps": [
            "⚠️ EXAM TRAP: Economies of scale means AWS is cheaper at scale — NOT that you must sign a contract.",
            "⚠️ EXAM TRAP: Automation saves money on labor — it does not make all AWS services free.",
            "⚠️ EXAM TRAP: Total Cost of Ownership (TCO) includes hidden on-prem costs like power and cooling, not just server sticker price.",
            "⚠️ EXAM TRAP: BYOL is about software licensing, not about bringing your own physical servers to AWS.",
        ],
    },
    "2.1": {
        "extra_points": [
            "📦 S3 — AWS manages infrastructure; you manage bucket policies, encryption settings, and who can access objects.",
            "⚡ Lambda — AWS manages runtime and patching; you manage function code and IAM execution role permissions.",
            "🗄️ RDS — AWS patches the database engine and OS; you manage data, schemas, and security groups.",
            "🖥️ EC2 — AWS manages physical host; YOU patch the guest operating system and installed applications.",
            "🔑 IAM is always YOUR responsibility — AWS never creates your users' passwords or access policies for you.",
        ],
        "comparisons": [
            {"title": "Security OF vs IN the cloud", "text": "OF = AWS secures data centers, hardware, and hypervisor. IN = you secure data, apps, network config, and access control."},
            {"title": "EC2 vs RDS vs Lambda responsibility", "text": "More managed = AWS patches more. EC2 = you patch OS. RDS = AWS patches DB engine. Lambda = AWS patches everything except your code."},
            {"title": "IaaS vs PaaS vs SaaS", "text": "IaaS (EC2) = you manage most. PaaS (RDS, Elastic Beanstalk) = AWS manages platform. SaaS (WorkMail) = AWS manages almost everything."},
            {"title": "Shared responsibility vs customer-only", "text": "Some things are always customer: data classification, IAM policies, encryption key management choices, and network traffic rules."},
        ],
        "traps": [
            "⚠️ EXAM TRAP: Physical security of data centers is ALWAYS AWS — never your job.",
            "⚠️ EXAM TRAP: You cannot ask AWS to patch your custom app code on EC2 — that is your responsibility.",
            "⚠️ EXAM TRAP: 'AWS encrypts all my data automatically' is wrong — you choose encryption settings for most services.",
            "⚠️ EXAM TRAP: Managed services shift MORE responsibility to AWS, not less. EC2 shifts LESS to AWS than Lambda.",
        ],
    },
    "2.2": {
        "extra_points": [
            "📜 AWS Artifact gives on-demand access to AWS compliance reports (SOC, PCI, ISO) — not your own audit reports.",
            "🔔 Amazon Macie discovers and protects sensitive data (like PII) in S3 using machine learning.",
            "🛡️ AWS Shield Advanced (paid) adds 24/7 DDoS response team — Shield Standard is free for everyone.",
            "🔐 KMS (Key Management Service) creates and controls encryption keys; CloudHSM provides dedicated hardware security modules.",
            "📋 AWS Audit Manager automates evidence collection for audits against compliance frameworks.",
        ],
        "comparisons": [
            {"title": "CloudTrail vs CloudWatch vs Config", "text": "CloudTrail = WHO did WHAT API call. CloudWatch = metrics and alarms on performance. Config = are resources compliant with rules."},
            {"title": "GuardDuty vs Inspector vs Security Hub", "text": "GuardDuty = threat detection from logs. Inspector = vulnerability scans on workloads. Security Hub = central dashboard for findings."},
            {"title": "Encryption at rest vs in transit", "text": "At rest = stored data (S3 SSE, EBS encryption). In transit = moving data (HTTPS/TLS via ACM certificates)."},
            {"title": "Artifact vs Audit Manager", "text": "Artifact = download AWS's compliance reports. Audit Manager = collect evidence that YOUR usage meets YOUR compliance goals."},
        ],
        "traps": [
            "⚠️ EXAM TRAP: CloudTrail logs API activity — it does NOT block attacks. WAF blocks web attacks.",
            "⚠️ EXAM TRAP: AWS Config checks resource configuration over time — it is not a firewall.",
            "⚠️ EXAM TRAP: Artifact provides AWS compliance documents — it does not automatically make YOUR app compliant.",
            "⚠️ EXAM TRAP: GuardDuty needs CloudTrail and VPC Flow Logs enabled to analyze threats — it does not replace them.",
        ],
    },
    "2.3": {
        "extra_points": [
            "📜 IAM policies are JSON documents that list Allow/Deny actions on resources — attach to users, groups, or roles.",
            "🔀 Permission boundaries set the MAX permissions an IAM entity can get — useful for delegating admin safely.",
            "🌐 IAM Identity Center (formerly AWS SSO) = single sign-on across multiple AWS accounts and business apps.",
            "🔄 Secrets Manager can auto-rotate database passwords; Parameter Store is cheaper for simple config values.",
            "🚫 Access keys for the root user are dangerous — create IAM users or roles for daily work instead.",
        ],
        "comparisons": [
            {"title": "IAM user vs role vs group", "text": "User = long-term person identity. Role = temporary credentials (for services or federation). Group = bundle users with shared permissions."},
            {"title": "IAM vs IAM Identity Center", "text": "IAM = users inside ONE account. Identity Center = one login across MANY accounts and SAML apps."},
            {"title": "Secrets Manager vs Parameter Store", "text": "Secrets Manager = secrets with automatic rotation (costs more). Parameter Store = config and simple secrets (free tier available)."},
            {"title": "Resource-based vs identity-based policies", "text": "Identity-based = attached to user/role ('I can access S3'). Resource-based = attached to resource ('this S3 bucket allows this role')."},
        ],
        "traps": [
            "⚠️ EXAM TRAP: IAM roles are for temporary credentials — never embed long-term access keys in Lambda or EC2 code.",
            "⚠️ EXAM TRAP: Root user should have MFA enabled and almost never used — IAM users/roles for daily tasks.",
            "⚠️ EXAM TRAP: IAM is global (not Regional) — policies apply across all Regions in the account.",
            "⚠️ EXAM TRAP: 'Deny' always wins over 'Allow' in IAM policy evaluation.",
        ],
    },
    "2.4": {
        "extra_points": [
            "🛡️ AWS Shield Standard protects against common DDoS at no extra cost on CloudFront, Route 53, and ELB.",
            "🧱 WAF works with CloudFront, ALB, and API Gateway — not raw EC2 instances directly.",
            "🔥 Network Firewall filters VPC traffic; Firewall Manager deploys WAF rules across many accounts.",
            "🔐 ACM (Certificate Manager) provides free TLS/SSL certificates for HTTPS on AWS services.",
            "📊 Trusted Advisor free checks: 7 core checks. Business/Enterprise Support unlocks all ~15+ checks.",
        ],
        "comparisons": [
            {"title": "WAF vs Shield vs Network Firewall", "text": "WAF = block web exploits (SQL injection). Shield = DDoS protection. Network Firewall = VPC-level traffic filtering."},
            {"title": "Security group vs NACL", "text": "Security group = stateful, instance ENI level, allow rules only. NACL = stateless, subnet level, allow AND deny rules."},
            {"title": "Trusted Advisor vs AWS Config", "text": "Trusted Advisor = best-practice recommendations (cost, security). Config = track if resources match YOUR defined rules."},
            {"title": "Marketplace vs AWS native security", "text": "Marketplace = third-party tools (firewalls, scanners). Native = WAF, GuardDuty, Shield built by AWS."},
        ],
        "traps": [
            "⚠️ EXAM TRAP: WAF protects web applications — it does NOT replace security groups for network access.",
            "⚠️ EXAM TRAP: Shield Standard is FREE — you do not need to 'enable' it; Advanced is the paid tier.",
            "⚠️ EXAM TRAP: Trusted Advisor full checks require Business or Enterprise Support — not Developer.",
            "⚠️ EXAM TRAP: Security groups are stateful (return traffic auto-allowed). NACLs are stateless (must allow both directions).",
        ],
    },
    "3.1": {
        "extra_points": [
            "🔧 AWS CLI uses the same APIs as the console — anything you click, you can script.",
            "📦 CloudFormation stacks can be updated, rolled back, and deleted as a unit — Infrastructure as Code.",
            "🌐 AWS Elastic Beanstalk = PaaS that handles deployment but you still control the underlying platform choices.",
            "📱 AWS Amplify helps front-end devs deploy web/mobile apps without deep AWS knowledge.",
            "🔁 Systems Manager (SSM) runs commands, patches, and session manager on EC2 without SSH keys.",
        ],
        "comparisons": [
            {"title": "Console vs CLI vs SDK vs CloudFormation", "text": "Console = manual clicks. CLI = terminal scripts. SDK = code in Python/Java/etc. CloudFormation = declarative templates for full stacks."},
            {"title": "Public vs private vs hybrid deployment", "text": "Public = AWS cloud. Private = on-premises only. Hybrid = VPN/Direct Connect linking your data center to AWS VPC."},
            {"title": "CloudFormation vs manual deployment", "text": "CloudFormation = repeatable, version-controlled, one-click rollback. Manual = fast for one-off but error-prone at scale."},
            {"title": "Elastic Beanstalk vs EC2", "text": "Beanstalk = AWS handles deployment and capacity. EC2 = you manage everything on the virtual server."},
        ],
        "traps": [
            "⚠️ EXAM TRAP: CloudFormation is Infrastructure as Code — it is NOT a monitoring tool (that is CloudWatch).",
            "⚠️ EXAM TRAP: Hybrid cloud means on-premises PLUS AWS connected — not 'multiple AWS Regions'.",
            "⚠️ EXAM TRAP: SDK is for application code; CLI is for scripts and automation from a terminal.",
            "⚠️ EXAM TRAP: You access AWS APIs from anywhere with valid credentials — not only from within a VPC.",
        ],
    },
    "3.2": {
        "extra_points": [
            "🌎 Each Region is independent — resources do not automatically replicate across Regions unless you set that up.",
            "🏢 AZs within a Region are connected by low-latency private fiber — use 2+ AZs for production workloads.",
            "📍 Local Zones put compute closer to cities; Wavelength extends AWS to 5G networks at the edge.",
            "🌍 Choose Region based on: latency to users, data sovereignty laws, service availability, and pricing.",
            "🔒 Some services are global (IAM, Route 53, CloudFront) while most are Regional (EC2, S3 buckets are Regional).",
        ],
        "comparisons": [
            {"title": "Region vs AZ vs Edge location", "text": "Region = geographic area. AZ = isolated data center(s) inside a Region. Edge = CloudFront cache point near users worldwide."},
            {"title": "Multi-AZ vs Multi-Region", "text": "Multi-AZ = high availability within one Region (survive AZ failure). Multi-Region = disaster recovery or global users (survive Region failure)."},
            {"title": "HA vs DR", "text": "High availability = stay up during component failure (usually Multi-AZ). Disaster recovery = recover after major outage (often Multi-Region)."},
            {"title": "Local Zone vs Edge location", "text": "Local Zone = full AWS compute/storage in a city. Edge location = lightweight cache for CloudFront content delivery."},
        ],
        "traps": [
            "⚠️ EXAM TRAP: Edge locations do NOT run your EC2 instances — they cache content for CloudFront.",
            "⚠️ EXAM TRAP: Multi-AZ is for availability within a Region, NOT for compliance with data residency in another country.",
            "⚠️ EXAM TRAP: AZs are NOT shared across Regions — us-east-1a and eu-west-1a are completely unrelated.",
            "⚠️ EXAM TRAP: Lowest latency to users usually means pick the Region closest to them, not always us-east-1.",
        ],
    },
    "3.3": {
        "extra_points": [
            "🖥️ EC2 instance families: General (t3/m5), Compute (c5), Memory (r5), Storage (i3), GPU (p4) — match workload to family.",
            "⚡ Lambda max 15-minute timeout — great for event-driven tasks, not long-running batch jobs.",
            "📦 Fargate = run containers without managing EC2 instances — pay for vCPU and memory used.",
            "🎯 Spot Instances can be interrupted with 2-minute warning — never use for critical databases.",
            "⚖️ ALB = layer 7 (HTTP), NLB = layer 4 (TCP/UDP, ultra-low latency), GLB = Gateway Load Balancer for security appliances.",
        ],
        "comparisons": [
            {"title": "EC2 vs Lambda vs Fargate", "text": "EC2 = full control, always-on servers. Lambda = event-driven, no server management, short runs. Fargate = containers without managing hosts."},
            {"title": "On-Demand vs Reserved vs Spot", "text": "On-Demand = flexible, full price. Reserved/Savings Plans = discount for commitment. Spot = cheapest, can be taken away."},
            {"title": "ECS vs EKS", "text": "ECS = AWS-native container orchestration. EKS = managed Kubernetes (portable, industry standard)."},
            {"title": "ALB vs NLB vs CLB", "text": "ALB = smart HTTP routing. NLB = millions of requests/sec, static IP. CLB (Classic) = legacy, avoid on new projects."},
        ],
        "traps": [
            "⚠️ EXAM TRAP: Spot Instances are CHEAP but INTERRUPTIBLE — wrong answer for a production database.",
            "⚠️ EXAM TRAP: Lambda is serverless compute — it is NOT for always-on web servers needing persistent connections.",
            "⚠️ EXAM TRAP: Dedicated Hosts give physical isolation for licensing — different from Dedicated Instances (just no sharing).",
            "⚠️ EXAM TRAP: Auto Scaling changes instance COUNT — rightsizing changes instance SIZE. Both are valid cost strategies.",
        ],
    },
    "3.4": {
        "extra_points": [
            "🗃️ RDS Multi-AZ = synchronous standby for failover (high availability). Read Replicas = scale read traffic asynchronously.",
            "⚡ DynamoDB single-digit millisecond latency at any scale — fully managed NoSQL key-value and document store.",
            "🧠 ElastiCache Redis supports persistence and complex data types; Memcached is simpler pure cache.",
            "📊 Redshift is columnar storage for analytics — not for transactional OLTP workloads.",
            "🔄 DMS supports homogeneous (same engine) and heterogeneous (different engines) migrations.",
        ],
        "comparisons": [
            {"title": "RDS vs DynamoDB", "text": "RDS = relational SQL, fixed schema, joins. DynamoDB = NoSQL, flexible schema, massive scale, serverless option."},
            {"title": "Multi-AZ vs Read Replica", "text": "Multi-AZ = automatic failover for writes (HA). Read Replica = extra copy for read scaling (not automatic write failover)."},
            {"title": "ElastiCache vs DAX", "text": "ElastiCache = general in-memory cache for apps. DAX = DynamoDB-specific microsecond read cache."},
            {"title": "Aurora vs RDS", "text": "Aurora = AWS-built MySQL/PostgreSQL compatible, faster storage, more replicas. RDS = standard managed open-source engines."},
        ],
        "traps": [
            "⚠️ EXAM TRAP: DynamoDB is NoSQL — it does NOT support traditional SQL joins across tables.",
            "⚠️ EXAM TRAP: Read Replicas are for READ scaling — they do NOT replace Multi-AZ for write failover.",
            "⚠️ EXAM TRAP: Redshift is a data WAREHOUSE — wrong choice for a shopping cart checkout database.",
            "⚠️ EXAM TRAP: DMS migrates data — SCT converts schemas. You often need BOTH for heterogeneous migrations.",
        ],
    },
    "3.5": {
        "extra_points": [
            "🏠 Every AWS account gets a default VPC — you can create custom VPCs with your own IP ranges (CIDR blocks).",
            "🌐 Internet Gateway = public internet access for VPC. NAT Gateway = outbound-only internet for private subnets.",
            "🔒 Security groups = virtual firewall on instances. NACLs = optional subnet-level firewall.",
            "🗺️ Route 53 routing policies: simple, weighted, latency, failover, geolocation, geoproximity, multi-value.",
            "🔌 Site-to-Site VPN = encrypted tunnel over internet. Direct Connect = dedicated private line (more consistent latency).",
        ],
        "comparisons": [
            {"title": "Public vs private subnet", "text": "Public = route to Internet Gateway (web servers). Private = no direct IGW route; use NAT Gateway for outbound updates."},
            {"title": "Security group vs NACL", "text": "SG = stateful, instance level, allow only. NACL = stateless, subnet level, allow and deny, evaluated in order."},
            {"title": "VPN vs Direct Connect", "text": "VPN = quick, encrypted, over public internet, lower cost. Direct Connect = dedicated line, higher bandwidth, consistent performance."},
            {"title": "Route 53 vs CloudFront", "text": "Route 53 = DNS (name to IP). CloudFront = CDN (cache content at edge). Often used together."},
        ],
        "traps": [
            "⚠️ EXAM TRAP: Private subnet instances need NAT Gateway (not IGW) to reach the internet for patches.",
            "⚠️ EXAM TRAP: Security groups are STATEFUL — return traffic is automatically allowed. NACLs are STATELESS.",
            "⚠️ EXAM TRAP: Route 53 registers domains AND routes DNS — it does not host your EC2 servers.",
            "⚠️ EXAM TRAP: VPC Peering connects two VPCs — it is NOT a VPN to your on-premises network.",
        ],
    },
    "3.6": {
        "extra_points": [
            "🪣 S3 Standard-IA and One Zone-IA cost less but charge retrieval fees — good for infrequent access.",
            "🧊 S3 Glacier Flexible Retrieval = minutes to hours. Glacier Deep Archive = cheapest, 12+ hour retrieval.",
            "💾 EBS volumes live in ONE AZ — snapshot to S3 for backup and copy to other AZs/Regions.",
            "📁 EFS scales automatically and can be mounted by many EC2 instances across AZs simultaneously.",
            "🌉 Storage Gateway types: File (NFS/SMB), Volume (iSCSI), Tape (virtual tapes to Glacier).",
        ],
        "comparisons": [
            {"title": "S3 vs EBS vs EFS", "text": "S3 = object storage via API (files, backups). EBS = block disk on ONE EC2. EFS = shared NFS file system across instances."},
            {"title": "S3 storage classes", "text": "Standard = frequent access. IA = infrequent. Glacier = archive. Intelligent-Tiering = auto-moves based on access patterns."},
            {"title": "EBS vs Instance Store", "text": "EBS = persistent network disk (survives stop/start). Instance Store = local physical disk (fast, lost if instance terminates)."},
            {"title": "Storage Gateway vs DataSync", "text": "Storage Gateway = on-prem apps access cloud storage as if local. DataSync = migrate/sync data to AWS online."},
        ],
        "traps": [
            "⚠️ EXAM TRAP: EBS is tied to ONE AZ — for shared file storage across instances, use EFS not EBS.",
            "⚠️ EXAM TRAP: S3 is object storage (HTTP API) — you cannot attach S3 as a boot disk to EC2.",
            "⚠️ EXAM TRAP: Glacier Deep Archive is cheapest but SLOWEST retrieval — wrong for daily access data.",
            "⚠️ EXAM TRAP: S3 has unlimited storage — EBS volumes have a max size per volume (though you can add more).",
        ],
    },
    "3.7": {
        "extra_points": [
            "🤖 SageMaker covers the full ML lifecycle: label data, train models, deploy endpoints, and monitor predictions.",
            "🔎 Athena queries S3 data with standard SQL — pay per query scanned (use columnar formats like Parquet to save money).",
            "🌊 Kinesis Data Streams = real-time ingestion. Kinesis Data Firehose = load streams into S3/Redshift automatically.",
            "🧩 Glue Data Catalog = metadata store; Glue ETL jobs transform data for analytics pipelines.",
            "📊 QuickSight = business intelligence dashboards — share interactive charts without building your own UI.",
        ],
        "comparisons": [
            {"title": "Athena vs Redshift", "text": "Athena = serverless SQL on S3 files, no cluster. Redshift = managed data warehouse cluster for heavy analytics."},
            {"title": "Kinesis vs SQS vs SNS", "text": "Kinesis = real-time streaming and analytics. SQS = decouple apps with message queues. SNS = pub/sub fan-out notifications."},
            {"title": "Glue vs EMR", "text": "Glue = serverless ETL and data catalog. EMR = managed Hadoop/Spark clusters for big data processing."},
            {"title": "Lex vs Connect", "text": "Lex = chatbot/voice AI engine. Connect = cloud call center that can USE Lex for automated phone menus."},
        ],
        "traps": [
            "⚠️ EXAM TRAP: Athena queries data IN S3 — it does not store data itself.",
            "⚠️ EXAM TRAP: Kinesis is for REAL-TIME streaming — batch analytics overnight belongs on Redshift or Athena.",
            "⚠️ EXAM TRAP: SageMaker is for building ML models — QuickSight is for visualizing business data.",
            "⚠️ EXAM TRAP: Kendra is enterprise SEARCH (find documents) — not a general chatbot (that is Lex).",
        ],
    },
    "3.8": {
        "extra_points": [
            "📨 SNS = push notifications to subscribers (email, SMS, Lambda, SQS). SQS = pull-based message queue.",
            "🔄 EventBridge = serverless event bus routing events between AWS services and SaaS apps.",
            "🛠️ CodePipeline orchestrates CI/CD; CodeBuild compiles/tests; CodeDeploy deploys to EC2/Lambda/ECS.",
            "🖥️ WorkSpaces = persistent virtual desktop (VDI). AppStream 2.0 = stream a single app to a browser.",
            "📡 IoT Core connects billions of devices and routes messages to Lambda, Kinesis, and other AWS services.",
        ],
        "comparisons": [
            {"title": "SNS vs SQS vs EventBridge", "text": "SNS = fan-out push to many subscribers. SQS = queue workers pull messages one at a time. EventBridge = route events on a bus with rules."},
            {"title": "SES vs SNS email", "text": "SES = bulk/marketing/transactional email at scale. SNS email = simple notification alerts to subscribers."},
            {"title": "WorkSpaces vs AppStream 2.0", "text": "WorkSpaces = full Windows/Linux desktop in the cloud. AppStream = stream one specific application, not the whole desktop."},
            {"title": "Amplify vs Elastic Beanstalk", "text": "Amplify = front-end focused (web/mobile hosting, auth, APIs). Beanstalk = deploy full back-end web applications."},
        ],
        "traps": [
            "⚠️ EXAM TRAP: SQS is PULL (consumer polls) — SNS is PUSH (delivers to subscribers immediately).",
            "⚠️ EXAM TRAP: SES is for EMAIL — SNS supports email but SES is the dedicated high-volume email service.",
            "⚠️ EXAM TRAP: X-Ray traces application performance — it does not deploy code (that is CodeDeploy).",
            "⚠️ EXAM TRAP: Connect is a CALL CENTER platform — not the same as SNS mobile push notifications.",
        ],
    },
    "4.1": {
        "extra_points": [
            "💳 On-Demand = zero commitment, highest per-hour cost — best for spiky or unknown workloads.",
            "📅 Savings Plans apply across compute (EC2, Lambda, Fargate) — more flexible than old Reserved Instances.",
            "🎯 Spot price changes with supply/demand — set max price or use Spot Fleet for diversification.",
            "📦 S3 Intelligent-Tiering auto-moves objects between tiers — small monitoring fee, no retrieval fees.",
            "🌐 Data transfer IN to AWS is usually free; OUT to internet and cross-Region costs money.",
        ],
        "comparisons": [
            {"title": "On-Demand vs Reserved vs Spot", "text": "On-Demand = flexible full price. Reserved/Savings = 1-3 year commitment discount. Spot = up to 90% off, interruptible."},
            {"title": "Savings Plans vs Reserved Instances", "text": "Savings Plans = flexible $/hour commitment across instance families. RIs = specific instance type/Region lock-in for deeper discount."},
            {"title": "S3 Standard vs IA vs Glacier", "text": "Standard = frequent access, instant. IA = infrequent, retrieval fee. Glacier = archive, minutes to hours retrieval."},
            {"title": "Dedicated Host vs Dedicated Instance", "text": "Dedicated Host = physical server you control for BYOL licensing. Dedicated Instance = your instances on isolated hardware, no host control."},
        ],
        "traps": [
            "⚠️ EXAM TRAP: Spot Instances are NOT for workloads that cannot tolerate interruption.",
            "⚠️ EXAM TRAP: Reserved Instances save money for STEADY-STATE usage — not for unpredictable spiky traffic.",
            "⚠️ EXAM TRAP: Data transfer OUT to the internet costs money — inbound data transfer is typically free.",
            "⚠️ EXAM TRAP: S3 Glacier is for ARCHIVE storage — wrong for a website users access every second.",
        ],
    },
    "4.2": {
        "extra_points": [
            "📊 Cost Explorer shows historical spend and can forecast future costs — free in the billing console.",
            "🚨 AWS Budgets can alert on actual OR forecasted spend — set monthly, daily, or custom thresholds.",
            "🏢 AWS Organizations consolidates billing and lets you apply SCPs (Service Control Policies) to limit what accounts can do.",
            "🏷️ Activate cost allocation tags in billing settings — tags alone do not appear in reports until activated.",
            "📋 Cost and Usage Report (CUR) = most detailed raw billing export — often loaded into Athena or QuickSight.",
        ],
        "comparisons": [
            {"title": "Cost Explorer vs Budgets vs Pricing Calculator", "text": "Explorer = analyze past/forecast spend. Budgets = alerts when thresholds hit. Calculator = estimate BEFORE deploying."},
            {"title": "CUR vs Cost Explorer", "text": "CUR = raw detailed line-item export for finance/BI. Cost Explorer = built-in visual charts and filters."},
            {"title": "Organizations vs consolidated billing", "text": "Consolidated billing = one bill, volume discounts. Organizations adds OU structure, SCPs, and cross-account management."},
            {"title": "Tags vs Cost Categories", "text": "Tags = labels on resources (team, env). Cost Categories = group costs into custom buckets in billing reports."},
        ],
        "traps": [
            "⚠️ EXAM TRAP: Pricing Calculator estimates FUTURE costs — Cost Explorer analyzes PAST and forecasted spend.",
            "⚠️ EXAM TRAP: Budgets send ALERTS — they do not automatically shut down resources (unless you add automation).",
            "⚠️ EXAM TRAP: Tags must be ACTIVATED as cost allocation tags to show in billing reports.",
            "⚠️ EXAM TRAP: AWS Organizations gives volume pricing discounts — it is not a separate paid product.",
        ],
    },
    "4.3": {
        "extra_points": [
            "🆓 Basic Support = free account and billing help, forums, docs — NO technical support cases or phone.",
            "👨‍💻 Developer Support = business-hours email access to Cloud Support Associates.",
            "🏢 Business Support = 24/7 phone/chat, <1 hour response for production system down, full Trusted Advisor.",
            "💚 AWS Health Dashboard shows personalized events affecting YOUR resources; Service Health Dashboard is public AWS-wide status.",
            "🤝 Solutions Architects (free) help design architectures; TAM (Enterprise) is a dedicated advisor.",
        ],
        "comparisons": [
            {"title": "Basic vs Developer vs Business vs Enterprise", "text": "Basic = free, no tech cases. Developer = email, business hours. Business = 24/7, faster response, full Trusted Advisor. Enterprise = TAM + concierge."},
            {"title": "Health Dashboard vs Personal Health Dashboard", "text": "Service Health = public status of all AWS services. AWS Health = account-specific alerts about YOUR affected resources."},
            {"title": "Trusted Advisor free vs paid", "text": "All accounts get 7 core checks. Business and Enterprise Support unlocks all checks including security and fault tolerance."},
            {"title": "re:Post vs Knowledge Center vs Documentation", "text": "re:Post = community Q&A. Knowledge Center = articles for common issues. Documentation = official service guides."},
        ],
        "traps": [
            "⚠️ EXAM TRAP: Basic Support does NOT include 24/7 phone support — that starts at Business Support.",
            "⚠️ EXAM TRAP: TAM (Technical Account Manager) comes with Enterprise Support — not Developer or Business alone.",
            "⚠️ EXAM TRAP: Service Health Dashboard is PUBLIC — AWS Health Dashboard is personalized to your account.",
            "⚠️ EXAM TRAP: Trusted Advisor FULL checks require Business or Enterprise Support — Developer only gets core checks.",
        ],
    },
}
