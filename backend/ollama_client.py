import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def ask_llm(prompt):
    res = requests.post(OLLAMA_URL, json={
        "model": "phi",
        "prompt": prompt,
        "stream": False
    })
    return res.json().get("response", "")
