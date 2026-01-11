from strands import Agent, tool
from agent.tools import list_stopped_instances, list_s3_buckets

@tool
def get_stopped_ec2():
    return list_stopped_instances()

@tool
def get_s3_buckets():
    return list_s3_buckets()


agent = Agent(
    name="aws-ops-agent",
    description="Helps answer questions about AWS resources using safe read-only tools",
    tools=[get_stopped_ec2, get_s3_buckets],
)
