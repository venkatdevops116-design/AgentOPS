# AIOps + AgenticOps POC

## Overview

This project demonstrates a working AIOps and AgenticOps Proof of Concept using:

* Flask Application
* Prometheus Monitoring
* Grafana Dashboard
* Ollama
* Llama 3.2
* Python Agent

---

# Architecture

```text
Flask App
    |
    v
Prometheus
    |
    v
Grafana
    |
    v
AgenticOps Assistant
    |
    v
Llama 3.2
```

---

# Prerequisites

* Docker Desktop
* Python 3.12+
* Ollama
* Llama 3.2 Model

Verify:

```bash
python --version
docker --version
ollama --version
```

---

# Project Structure

```text
aiops-agenticops-poc/

├── app.py
├── agent.py
├── agentic_agent.py
├── Dockerfile
├── docker-compose.yml
├── prometheus.yml
├── requirements.txt
└── README.md
```

---

# Start Environment

Navigate to project:

```bash
cd /d/AI-proje/aiops-agenticops-poc
```

Build and start:

```bash
docker compose up --build -d
```

Verify:

```bash
docker ps
```

Expected Containers:

* Flask App
* Prometheus
* Grafana

---

# Verify Application

Open:

```text
http://localhost:5000
```

Expected:

```text
Order Service Running
```

Metrics:

```text
http://localhost:5000/metrics
```

---

# Verify Prometheus

Open:

```text
http://localhost:9090
```

Query:

```promql
request_count_total
```

---

# Verify Grafana

Open:

```text
http://localhost:3000
```

Login:

```text
admin
admin
```

Add Data Source:

```text
http://prometheus:9090
```

Create Dashboard Query:

```promql
request_count_total
```

---

# Generate Traffic

Git Bash:

```bash
for i in {1..100}
do
curl http://localhost:5000
done
```

Prometheus metric should increase.

---

# Verify Ollama

Installed Models:

```bash
ollama list
```

Test Model:

```bash
ollama run llama3.2
```

Example:

```text
What is AIOps?
```

---

# Test Ollama API

```bash
python test_ollama.py
```

Expected:

AI-generated response from Llama 3.2

---

# Run AgenticOps Assistant

```bash
python agentic_agent.py
```

Example Questions:

```text
Summarize system health

Why is my application slow?

What incidents occurred today?

What operational risks exist?
```

---

# Scenario 1: Traffic Spike

Generate Traffic:

```bash
for i in {1..500}
do
curl http://localhost:5000
done
```

Ask:

```text
Why is my application slow?
```

Expected:

Traffic spike analysis and recommendations.

---

# Scenario 2: Database Failure

Endpoint:

```text
http://localhost:5000/error
```

Generate errors.

Ask:

```text
What incidents occurred today?
```

Expected:

Root Cause Analysis and recommendations.

---

# Scenario 3: Disk Space Alert

Example:

```text
Disk Free Space = 47 MB
```

Ask:

```text
What operational risks exist?
```

Expected:

Storage risk analysis.

---

# Scenario 4: CPU Saturation

Metrics:

```text
CPU Usage = 90%
Memory Usage = 80%
```

Ask:

```text
Summarize system health.
```

Expected:

Capacity and performance recommendations.

---

# Demo Flow

1. Start Docker
2. Open Grafana
3. Generate Traffic
4. Show Metrics
5. Run AgenticOps Agent
6. Ask RCA Questions
7. Show AI Recommendations

---

# Business Benefits

* Faster Incident Resolution
* Reduced MTTR
* Proactive Monitoring
* AI-assisted RCA
* Improved Reliability

---

# Future Enhancements

* Log Analysis
* Tracing
* Auto Remediation
* ServiceNow Integration
* Multi-Agent Architecture
* Autonomous Operations

---

# Technology Stack

* Python
* Flask
* Docker
* Prometheus
* Grafana
* Ollama
* Llama 3.2

---

# Author

AIOps + AgenticOps Proof of Concept
Local Deployment using Docker and Ollama

```
```

