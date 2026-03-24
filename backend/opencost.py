import requests

OPENCOST_URL = "http://localhost:9003/allocation?window=1h"

def get_cost_data():
    res = requests.get(OPENCOST_URL, timeout=5)
    data = res.json()

    workloads = []

    for block in data.get("data", []):
        for name, value in block.items():
            namespace = value.get("properties", {}).get("namespace", "unknown")

            # ❗ Skip system pods (optional but recommended)
            if namespace == "kube-system":
                continue

            workloads.append({
                "workload": name,
                "namespace": namespace,
                "cpuCost": round(value.get("cpuCost", 0), 5),
                "ramCost": round(value.get("ramCost", 0), 5),
                "totalCost": round(value.get("totalCost", 0), 5)
            })

    # sort highest cost first
    workloads = sorted(workloads, key=lambda x: x["totalCost"], reverse=True)

    return workloads