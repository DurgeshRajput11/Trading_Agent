# CrowdWisdomTrading – Crypto Prediction Agent System

A modular **multi-agent backend system** for short-term crypto prediction, risk management, and decision-making.

## Project Overview

This project implements a **multi-agent architecture** to predict short-term (5-minute) crypto price movements and make disciplined trading decisions.

The system integrates:
- Real-time market data (Binance)
- Prediction logic
- Risk management (Kelly Criterion)
- Feedback loop
- LLM-based explanation (OpenRouter)
- External tool integration (Apify)

---

## ⚙️ Tech Stack

- Python  
- Binance API  
- Apify  
- OpenRouter  
- NumPy  
- Custom Agent Architecture (Hermes-style)  

---

## System Architecture

```
                 HermesController
                        ↓
     ┌────────────── Pipeline ───────────────┐
     ↓                                       ↓
Search → Data → Prediction → Risk → Feedback → Output
                                                ↓
                                       LLM Explanation
```

---

## Agents Description

### 🔍 SearchAgent
- Identifies crypto assets (BTC, ETH)

### DataAgent
- Fetches real-time OHLC data from Binance API

### 📈 PredictionAgent
- Uses moving average strategy  
- Outputs:
  - `UP` or `DOWN`
  - Confidence score

###  RiskAgent
- Applies **Kelly Criterion**
- Caps exposure to prevent over-risking

### 🔄 FeedbackAgent
- Tracks prediction accuracy
- Simulates learning loop

###  HermesController
- Orchestrates agent execution
- Controls pipeline flow

---

## 🔗 External Integrations

###  Apify
- Executes actors programmatically
- Demonstrates tool integration capability

###  OpenRouter
- Generates explanation for predictions
- Used for reasoning (not prediction)

---

##  How to Run

### 1. Clone repository
```bash
git clone <your-repo-link>
cd project
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add environment variables
Create a `.env` file:
```env
APIFY_TOKEN=your_apify_token
OPENROUTER_API_KEY=your_openrouter_key
```

### 4. Run the project
```bash
python main.py
```

---

##  Sample Output

```
ASSET | PRED | CONF | BET
------|------|------|------
BTC   | DOWN | 0.58 | 16.0%
ETH   | UP   | 0.58 | 16.0%

LLM: Prediction explanation...
```

---

##  Key Design Decisions

- Used Binance API instead of scraping for reliability
- Used Apify to demonstrate scalable integration
- LLM used only for reasoning, not prediction
- Risk-first approach using Kelly Criterion

---

##  Insights

- Prediction accuracy alone is not enough
- Risk management is critical
- System focuses on decision-making under uncertainty

---

##  Future Improvements

- Integrate Kronos model
- Multi-timeframe analysis
- Real trading execution
- Dashboard visualization
- Better feedback learning

---

## 👤 Author

**Durgesh Singh**  
IIIT Una

---


## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---
