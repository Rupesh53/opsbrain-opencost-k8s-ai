#  AI-Powered Kubernetes Cost Advisor (OpenCost + LLM)

An intelligent FinOps + AI system that analyzes Kubernetes pod-level
costs using OpenCost and provides cost optimization suggestions using a
local LLM (Ollama).

## 🧠 Architecture

Kubernetes → Prometheus → OpenCost → FastAPI → Ollama → React

## ⚙️ Prerequisites

-   Docker Desktop (Kubernetes enabled)
-   kubectl
-   Helm
-   Python 3.10+
-   Node.js
-   Ollama

## 🧱 Step 1: Install Prometheus

helm repo add prometheus-community
https://prometheus-community.github.io/helm-charts helm install
prometheus prometheus-community/kube-prometheus-stack --set
prometheus-node-exporter.enabled=false

## 💸 Step 2: Install OpenCost

helm repo add opencost https://opencost.github.io/opencost-helm-chart
helm install opencost opencost/opencost\
--set opencost.prometheus.internal.enabled=false\
--set opencost.prometheus.external.enabled=true\
--set
opencost.prometheus.external.url=http://prometheus-kube-prometheus-prometheus.default.svc.cluster.local:9090

## 🔍 Step 3: Verify

kubectl port-forward svc/opencost 9003:9003 curl
"http://localhost:9003/allocation?window=1h"

## ⚡ Step 4: Sample Workload

kubectl create deployment myapp --image=nginx kubectl expose deployment
myapp --port=80

## 🧠 Backend

cd backend pip install -r requirements.txt uvicorn main:app --reload

## 🤖 LLM

ollama run phi3

## 🎨 Frontend

cd frontend npm install npm start

## 💬 Queries

-   Which pod is costing most?
-   How can I reduce cost?

## 📊 Features

-   Pod-level cost
-   AI suggestions
-   Fast API + React UI

## 🚀 Future

-   Charts
-   Slack bot
-   AKS deployment

## 👨‍💻 Author

Rupesh Nayak
