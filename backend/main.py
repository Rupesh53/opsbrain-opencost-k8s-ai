from fastapi import FastAPI
from agent import run_agent

app = FastAPI()

@app.post("/chat")
def chat(data: dict):
    query = data.get("query")
    response = run_agent(query)
    return {"response": response}
