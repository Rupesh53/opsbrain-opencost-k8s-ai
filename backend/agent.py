from opencost import get_cost_data
from ollama_client import ask_llm

def run_agent(query):
    cost_data = get_cost_data()

    if not cost_data:
        return "⚠️ No workload cost data available yet."
    
    if "costing most" in query.lower():
        top = cost_data[0]
        return f"{top['workload']} (ns: {top['namespace']}) costs highest: ${top['totalCost']}"
    # take top 10 for LLM (important for speed)
    top_workloads = cost_data[:10]
    formatted = "\n".join([
    f"- Pod: {w['workload']} | Namespace: {w['namespace']} | Cost: ${w['totalCost']}"
    for w in top_workloads
    ])
    print("Testing with LLM ")
    prompt = f"""
You are a Kubernetes FinOps expert.

Here is pod cost data:
{formatted}

Tasks:
1. List top costly pods
2. Explain why they cost more
3. Suggest how to reduce cost

Give output in clean bullet points.
"""

    return ask_llm(prompt)