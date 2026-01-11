import streamlit as st
from agent.agent import agent

st.set_page_config(page_title="AWS Ops Agent", layout="centered")

st.title("🤖 AWS Ops Agent (Agentic AI on Bedrock)")
st.caption("Ask about your AWS infrastructure using natural language")

if "history" not in st.session_state:
    st.session_state.history = []

query = st.text_input("Ask a question about AWS:")

if st.button("Run") and query:
    with st.spinner("Agent thinking..."):
        result = agent(query)
        answer = str(result)

    st.session_state.history.append((query, answer))

for q, a in reversed(st.session_state.history):
    st.markdown(f"### 🧑 You:\n{q}")
    st.markdown(f"### 🤖 Agent:\n{a}")
    st.markdown("---")
