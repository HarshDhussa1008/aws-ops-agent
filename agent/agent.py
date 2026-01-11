from dotenv import load_dotenv
from strands import Agent, tool
from strands.models import BedrockModel
from agent.tools import list_stopped_instances, list_s3_buckets
import os

load_dotenv()

@tool
def get_stopped_ec2():
    return list_stopped_instances()

@tool
def get_s3_buckets():
    return list_s3_buckets()

# Bedrock LLM configuration
model = BedrockModel(
    model_id=os.getenv("BEDROCK_MODEL_ID"),
    region_name=os.getenv("AWS_DEFAULT_REGION"),
)

SYSTEM_PROMPT = """
You are an AWS Operations Assistant.
Rules:
- Use tools to answer questions about AWS resources.
- Never perform destructive actions.
- If unsure, ask for clarification.
- Always explain what you did.
"""

agent = Agent(
    name="aws-ops-agent",
    description="Helps answer questions about AWS resources using safe read-only tools",
    system_prompt=SYSTEM_PROMPT,
    tools=[get_stopped_ec2, get_s3_buckets],
    model=model
)
