from opencost import get_cost_data
from ollama_client import ask_llm

def run_agent(query):
    cost_data = get_cost_data()

    prompt = f"""
You are a Kubernetes cost optimization expert.

User question: {query}

Cost data:
{cost_data}

Give clear suggestions to reduce cost.
"""

    return ask_llm(prompt)
