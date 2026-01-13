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


def classify_intent(query: str):
    """
    Classify user intent into READ or ACTION.
    """
    action_keywords = ["start", "stop", "restart", "terminate", "delete", "modify"]

    if any(word in query.lower() for word in action_keywords):
        return {"intent": "ACTION"}
    return {"intent": "READ"}


def start_ec2_instance(instance_id: str):
    """
    Start an EC2 instance (requires approval).
    """
    response = ec2.start_instances(InstanceIds=[instance_id])
    print(f"🛠 Tool called: start_ec2_instance for {instance_id} - {response}")
    return {"status": "STARTED", "instance_id": instance_id}