import requests

PROM_URL = "http://localhost:9090"

r = requests.get(
    f"{PROM_URL}/api/v1/query",
    params={"query": "request_count_total"}
)

data = r.json()["data"]["result"]

if not data:
    print("No metrics found yet.")
    print("Generate traffic first:")
    print("curl http://localhost:5000")
    exit()

value = float(data[0]["value"][1])

print(f"Requests = {value}")

if value > 50:
    print("AI Agent: High traffic detected")
else:
    print("AI Agent: System healthy")
