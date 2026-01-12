from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_aws import BedrockEmbeddings
import os
load_dotenv()


embeddings = BedrockEmbeddings(
    region_name=os.getenv("AWS_DEFAULT_REGION", "ap-south-1"),
    model_id=os.getenv('RAG_EMBEDDING_MODEL')
)

sop_db = FAISS.load_local(
    "rag/store",
    embeddings,
    allow_dangerous_deserialization=True
)