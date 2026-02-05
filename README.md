# Agentic Honey-Pot for Scam Detection & Intelligence Extraction

This project implements an AI-powered agentic honeypot that detects scam messages
and autonomously engages scammers to extract actionable intelligence.

## 🚀 Features
- Scam intent detection
- Autonomous multi-turn engagement
- Extraction of UPI IDs, bank account numbers, and phishing URLs
- Secure API with API-key authentication
- Robust handling of malformed or empty requests
- Deployed as a public FastAPI service

## 🧠 How It Works
1. Incoming messages are analyzed for scam intent
2. Once detected, an AI agent responds with a believable persona
3. Scam-related intelligence is extracted and accumulated
4. Structured JSON output is returned for evaluation

## 🔐 Authentication
All requests require:
