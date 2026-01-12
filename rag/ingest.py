import os
from dotenv import load_dotenv
from langchain_text_splitters  import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_aws import BedrockEmbeddings

DOCS_PATH = "rag/docs"
STORE_PATH = "rag/store"
load_dotenv()


def ingest():
    texts = []
    for fname in os.listdir(DOCS_PATH):
        with open(os.path.join(DOCS_PATH, fname), "r", encoding="utf-8") as f:
            texts.append(f.read())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )
    docs = splitter.create_documents(texts)
    
    model = os.getenv('RAG_EMBEDDING_MODEL')
    print(f"Using {model} for embeddings")

    embeddings = BedrockEmbeddings(
        model_id=model,
        region_name=os.getenv("AWS_DEFAULT_REGION", "ap-south-1")
    )

    db = FAISS.from_documents(docs, embeddings)
    db.save_local(STORE_PATH)
    print("✅ SOP vector store built")

if __name__ == "__main__":
    ingest()
