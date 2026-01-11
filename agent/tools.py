import boto3

ec2 = boto3.client("ec2")
s3 = boto3.client("s3")

def list_stopped_instances():
    """List all stopped EC2 instances"""
    
    print("🛠 Tool called: list_stopped_instances")
    resp = ec2.describe_instances(
        Filters=[{"Name": "instance-state-name", "Values": ["stopped"]}]
    )
    ids = []
    for r in resp["Reservations"]:
        for i in r["Instances"]:
            ids.append(i["InstanceId"])
    return {"stopped_instances": ids}

def list_s3_buckets():
    """List all S3 buckets"""
    
    print("🛠 Tool called: list_s3_buckets")
    resp = s3.list_buckets()
    return {"buckets": [b["Name"] for b in resp["Buckets"]]}
