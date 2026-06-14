import requests

# Get Prometheus metric
prom = requests.get(
    "http://localhost:9090/api/v1/query",
    params={"query": "request_count_total"}
).json()

results = prom["data"]["result"]

if results:
    requests_count = results[0]["value"][1]
else:
    requests_count = "0"

question = input("Ask your question: ")

prompt = f"""
You are a Senior SRE Engineer.

Current Metrics:
request_count_total = {requests_count}

Question:
{question}

Provide:
1. System Health
2. Root Cause Analysis
3. Risks
4. Recommendations
"""

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    },
    timeout=120
)

print("\n===== AGENTICOPS ANALYSIS =====\n")
print(response.json()["response"])
