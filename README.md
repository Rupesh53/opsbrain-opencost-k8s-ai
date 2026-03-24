# K8s Cost AI Advisor (Ollama + OpenCost)

## Steps

1. Start Ollama:
   ollama run llama3

2. Start OpenCost:
   helm install opencost opencost/opencost

3. Run backend:
   cd backend && uvicorn main:app --reload

4. Run frontend:
   cd frontend && npm install && npm start
