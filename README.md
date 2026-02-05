
# Agentic Honey-Pot for Scam Detection & Intelligence Extraction

This project implements an AI-powered Agentic Honeypot system that detects scam
messages and autonomously engages scammers to extract actionable intelligence such
as bank account numbers, UPI IDs, and phishing URLs.

Built and deployed as part of the **India AI Impact Buildathon** under the
“AI for Fraud Detection & User Safety” challenge.

---

## 🚀 Key Features
- Scam intent detection from incoming messages
- Autonomous agent-based engagement after detection
- Multi-turn conversation handling using conversation IDs
- Extraction of:
  - UPI IDs
  - Bank account numbers
  - Phishing URLs
- Secure API using API-key authentication
- Robust handling of malformed / empty requests
- Public deployment with stable uptime

---

## 🧠 System Flow
1. Incoming messages are received via API
2. Scam intent is detected using keyword analysis
3. An autonomous agent responds with a believable human persona
4. Scam intelligence is extracted and accumulated
5. Structured JSON output is returned for evaluation

---

## 🔐 Authentication
All requests must include the following header:

```

x-api-key: <API_KEY>

````

---

## 📡 API Endpoint

### POST /honeypot

#### Example Request
```json
{
  "message": "Your account is blocked. Send your UPI immediately",
  "conversation_id": "conv_001"
}
````

#### Example Response

```json
{
  "scam_detected": true,
  "engagement": {
    "turns": 1,
    "duration_seconds": 2
  },
  "extracted_intelligence": {
    "upi_ids": [],
    "bank_accounts": [],
    "phishing_urls": []
  },
  "response": "I am not very good with these things, can you explain again?"
}
```

---

## 🛠 Tech Stack

* Python
* FastAPI
* Regex-based intelligence extraction
* Render (deployment)

---

## 🌍 Deployment

The API is deployed as a public endpoint and tested using the official
Honeypot Endpoint Tester provided by the hackathon.

---

## 🏁 Status

✅ Endpoint tested and validated
✅ Successfully submitted for automated evaluation

```

