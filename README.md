
# 🛡️ Agentic Honey-Pot for Scam Detection & Intelligence Extraction

This project implements an **AI-powered Agentic Honeypot system** that detects scam
messages and autonomously engages scammers to extract actionable intelligence such
as **bank account numbers, UPI IDs, and phishing URLs**.

Built and deployed as part of the **India AI Impact Buildathon** under the  
**AI for Fraud Detection & User Safety** challenge.

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
- Robust handling of malformed or empty requests
- Public deployment with stable uptime
- Endpoint validated using official hackathon tester

---

## 🧠 System Flow
1. Incoming messages are received via an API
2. Scam intent is detected using keyword-based logic
3. An autonomous agent responds with a believable human persona
4. Scam intelligence is extracted and accumulated
5. Structured JSON output is returned for evaluation

---

## 🏗 System Architecture

```

Client / Scammer Simulator
│
▼
┌──────────────────────────┐
│  FastAPI Honeypot API    │
│  (POST /honeypot)        │
└──────────┬───────────────┘
│
▼
┌──────────────────────────┐
│  Scam Detection Engine   │
│  (Keyword-based logic)   │
└──────────┬───────────────┘
│ scam detected
▼
┌──────────────────────────┐
│  Agentic Response Module │
│  (Believable persona)    │
└──────────┬───────────────┘
│
▼
┌──────────────────────────┐
│ Intelligence Extractor   │
│ - UPI IDs                │
│ - Bank Accounts          │
│ - Phishing URLs          │
└──────────┬───────────────┘
│
▼
┌──────────────────────────┐
│ Structured JSON Output   │
│ (Metrics + Intelligence) │
└──────────────────────────┘

```

---

## 🔐 Authentication
All requests must include the following HTTP header:

```

x-api-key: <API_KEY>

````

Requests without a valid API key are rejected with `401 Unauthorized`.

---

## 📡 API Endpoint

### `POST /honeypot`

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

* **Python**
* **FastAPI**
* Regex-based intelligence extraction
* Render (cloud deployment)

---

## 🌍 Deployment

The API is deployed as a **public endpoint** and validated using the official
**Agentic Honey-Pot Endpoint Tester** provided by the hackathon platform.

---

## 🧪 Testing & Validation

* Local testing using Swagger UI (`/docs`)
* Public endpoint tested via hackathon-provided tester
* Handles:

  * Empty request bodies
  * Missing or malformed JSON
  * Unexpected input types
  * Repeated and multi-turn requests

---

## 🔮 Future Improvements

* Integrate LLM-based agents (GPT / open-source LLMs) for smarter engagement
* Add long-term memory for adaptive multi-turn scam conversations
* Replace keyword-based detection with ML-based classifiers
* Persist extracted intelligence in a database for large-scale analysis
* Add rate limiting, logging, and monitoring for production use
* Support multilingual scam detection

---

## 🏁 Status

✅ Endpoint tested and validated
✅ Successfully submitted for automated evaluation
✅ Production-hardened and evaluator-safe

---

## 📌 Author Notes

This project demonstrates real-world considerations such as:

* Secure API design
* Agentic system behavior
* Robust error handling
* Cloud deployment and evaluation readiness




