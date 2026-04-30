#  Multi-Timeframe Crypto Trading System (Hermes Framework)

##  Overview

This project implements a rule-based crypto trading system using a multi-agent architecture.
The system analyzes market data across multiple timeframes (1m and 5m) and generates trading decisions based on trend strength, momentum, and risk control.

The goal is **not to trade frequently**, but to trade **only when signals are meaningful and risk is controlled**.

---

##  Core Idea

The system follows a simple but realistic trading philosophy:

* Avoid trades in **sideways markets**
* Prefer **trend confirmation across timeframes**
* Allow **early entries with reduced confidence**
* Scale bet size based on **confidence and risk**

---

##  Architecture

The system is divided into modular agents:

### 1. SearchAgent

* Identifies assets to trade (currently BTC, ETH)

### 2. DataAgent

* Fetches real-time market data from Binance API
* Supports multiple timeframes (1m, 5m)

### 3. PredictionAgent

* Computes indicators:

  * Moving Averages (short vs long)
  * RSI (Relative Strength Index)
  * ADX (trend strength)
* Generates:

  * Prediction → `UP / DOWN / NO TRADE`
  * Confidence score (dynamic)

---

### 4. HermesController (Core Logic)

Combines multi-timeframe signals:

| Scenario                 | Action                           |
| ------------------------ | -------------------------------- |
| Both NO TRADE            | Skip                             |
| Strong conflict          | Skip                             |
| Weak conflict            | Allow trade (reduced confidence) |
| Higher timeframe missing | Skip                             |
| Both agree               | Strong trade                     |

---

### 5. RiskAgent

* Calculates bet size using confidence
* Reduces exposure when:

  * Confidence is low
  * RSI is extreme (overbought/oversold)

---

### 6. FeedbackAgent

* Simulates trade outcome (for evaluation)
* Used to track accuracy

---

## ⚙️ Trading Logic

###  Trade is taken when:

* Confidence ≥ **0.45**
* Market is not sideways (ADX filter)
* No strong conflict between timeframes

---

###  Trade is skipped when:

* Market is sideways (low ADX)
* Signals are too weak
* Strong disagreement across timeframes

---

## Confidence Calculation

Confidence is computed using:

* Moving average difference
* Momentum
* Trend strength (ADX)

It is:

* Dynamic (changes every run)
* Clamped between **0.3 and 0.9**
* Slightly randomized to avoid deterministic outputs

---

##  Risk Management

* Position size capped at **10%**
* Reduced for:

  * Confidence < 0.65
  * Extreme RSI conditions

---

##  Sample Output

```
ASSET | PRED | CONF | BET
BTC   | NO TRADE | 0 | 0%
ETH   | DOWN     | 0.54 | 1.4%
Reason → WEAK_CONFLICT | 1m(DOWN) & 5m(UP)
```

---

##  Key Features

* Multi-timeframe confirmation
* Sideways market detection (ADX)
* Conflict-aware decision making
* Dynamic confidence scoring
* Risk-adjusted position sizing
* Modular agent-based design

---

##  Limitations

* No historical backtesting
* No real profit tracking
* Indicators are simplified (not production-grade)
* Feedback is simulated (random)

---

##  Future Improvements

* Add backtesting engine
* Replace rules with ML model
* Portfolio selection (choose best asset)
* Real-time deployment
* Sharpe ratio / drawdown metrics

---

##  Conclusion

This system demonstrates:

* Practical understanding of trading logic
* Risk-aware decision making
* Multi-timeframe analysis
* Modular system design

It prioritizes **consistency and safety over overtrading**, making it closer to real-world trading systems than naive approaches.

---

## 👨‍💻 Author

Durgesh Singh
