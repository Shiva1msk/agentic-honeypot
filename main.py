from fastapi import FastAPI, Request, Header, HTTPException
import re
import time
import os

app = FastAPI()

# API key from environment
API_KEY = os.getenv("API_KEY")

# In-memory conversation store
conversations = {}

# ---------- Scam Detection ----------
def detect_scam(message: str) -> bool:
    scam_keywords = [
        "otp", "verify", "account", "blocked", "kyc",
        "urgent", "upi", "link", "bank"
    ]
    message = message.lower()
    return any(word in message for word in scam_keywords)

# ---------- Intelligence Extraction ----------
def extract_intelligence(text: str):
    upi_pattern = r"[a-zA-Z0-9.\-_]{2,}@[a-zA-Z]{2,}"
    bank_pattern = r"\b\d{9,18}\b"
    url_pattern = r"https?://[^\s]+"

    return {
        "upi_ids": re.findall(upi_pattern, text),
        "bank_accounts": re.findall(bank_pattern, text),
        "phishing_urls": re.findall(url_pattern, text)
    }

# ---------- Agent Reply ----------
def agent_reply():
    replies = [
        "I am not very good with these things, can you explain again?",
        "I tried but it is not working, what should I do now?",
        "Which account is this related to?",
        "Can you send the details once more?"
    ]
    return replies[int(time.time()) % len(replies)]

# ---------- Honeypot API ----------
@app.post("/honeypot")
async def honeypot(
    request: Request,
    x_api_key: str = Header(None)
):
    # API key validation
    if API_KEY is None or x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    # BULLETPROOF BODY HANDLING
    body = await request.body()
    if body:
        try:
            data = await request.json()
        except:
            data = {}
    else:
        data = {}

    # FORCE message to always be a string
    raw_message = data.get("message", "")
    message = str(raw_message)

    conversation_id = str(data.get("conversation_id", "default"))

    # Initialize conversation
    if conversation_id not in conversations:
        conversations[conversation_id] = {
            "start_time": time.time(),
            "turns": 0,
            "intelligence": {
                "upi_ids": [],
                "bank_accounts": [],
                "phishing_urls": []
            }
        }

    convo = conversations[conversation_id]
    convo["turns"] += 1

    # Scam detection
    scam_detected = detect_scam(message)

    # Intelligence extraction
    extracted = extract_intelligence(message)
    for key in extracted:
        convo["intelligence"][key].extend(extracted[key])

    # Agent response
    response_message = (
        agent_reply()
        if scam_detected
        else "Sorry, can you please clarify?"
    )

    # Final response
    return {
        "scam_detected": scam_detected,
        "engagement": {
            "turns": convo["turns"],
            "duration_seconds": int(time.time() - convo["start_time"])
        },
        "extracted_intelligence": convo["intelligence"],
        "response": response_message
    }
