from agent.agent import agent

print("AWS Ops Agent (AgentCore + Strands)")
while q := input(">> "):
    if q.lower() in {"exit", "quit"}:
        break
    result = agent(q)
    print("\nAnswer:\n", result, "\n")