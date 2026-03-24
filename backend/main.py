from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from agent import run_agent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
def chat(data: dict):
    query = data.get("query")
    response = run_agent(query)
    print("Enter the chat backend")
    return {"response": response}