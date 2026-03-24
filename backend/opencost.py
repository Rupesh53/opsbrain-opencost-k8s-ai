import requests

OPENCOST_URL = "http://localhost:9003/allocation"

def get_cost_data():
    try:
        res = requests.get(OPENCOST_URL)
        data = res.json()

        workloads = []
        for k, v in data.get("data", {}).items():
            workloads.append({
                "name": k,
                "cost": round(v.get("cost", 0), 2)
            })

        return workloads
    except Exception as e:
        return [{"error": str(e)}]
