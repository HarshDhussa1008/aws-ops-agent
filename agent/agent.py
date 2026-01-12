from dotenv import load_dotenv
from strands import Agent, tool
from strands.models import BedrockModel
from agent.tools import list_stopped_instances, list_s3_buckets
import os
from agent.rag import sop_db

load_dotenv()

@tool
def get_stopped_ec2():
    return list_stopped_instances()

@tool
def get_s3_buckets():
    return list_s3_buckets()

@tool
def search_sop(query: str):
    """Search SOP and runbook knowledge base"""
    docs = sop_db.similarity_search(query, k=3)
    return {
        "sop_matches": [d.page_content for d in docs]
    }

# Bedrock LLM configuration
model = BedrockModel(
    model_id=os.getenv("BEDROCK_MODEL_ID"),
    region_name=os.getenv("AWS_DEFAULT_REGION"),
)

SYSTEM_PROMPT = """
You are an AWS Operations Assistant.
Rules:
- Use tools to answer questions about AWS resources.
- Use SOP search when explaining causes or next steps.
- Never perform destructive actions.
- If unsure, ask for clarification.
- You MUST always produce the final answer by combining:
  1. AWS findings returned by AWS tools
  2. SOP guidance returned by SOP tools
- Never skip AWS findings if they were retrieved.
"""

agent = Agent(
    name="aws-ops-agent",
    description="Helps answer questions about AWS resources using safe read-only tools",
    system_prompt=SYSTEM_PROMPT,
    tools=[get_stopped_ec2, get_s3_buckets, search_sop],
    model=model
)
