from utils.logger import get_logger

logger = get_logger("HermesController")

class HermesController:
    def __init__(self, search, data, predictor, risk, feedback):
        self.search = search
        self.data = data
        self.predictor = predictor
        self.risk = risk
        self.feedback = feedback

    def run(self):
        logger.info("Starting Hermes-style loop")

        markets = self.search.run()
        results = []

        for asset in markets:
            data_1m = self.data.fetch_data(asset, "1m")
            data_5m = self.data.fetch_data(asset, "5m")

            if not data_1m or not data_5m:
                continue

            pred_1m = self.predictor.predict(data_1m)
            pred_5m = self.predictor.predict(data_5m)

            d1 = pred_1m["prediction"]
            d5 = pred_5m["prediction"]

          
            if d1 == "NO TRADE" and d5 == "NO TRADE":
                results.append(self.no_trade(asset, "No signal"))
                continue

         
            if d1 != "NO TRADE" and d5 != "NO TRADE" and d1 != d5:

           
                if pred_5m["confidence"] > 0.7:
                    results.append(self.no_trade(asset, "Strong conflict"))
                    continue

            
                prediction = d1
                confidence = pred_1m["confidence"] * 0.7
                confidence = round(confidence, 2)
                strength = "WEAK_CONFLICT"

         
            elif d5 == "NO TRADE":
                results.append(self.no_trade(asset, "Waiting HTF"))
                continue

        
            else:
                prediction = d5
                confidence = round(
                    0.6 * pred_5m["confidence"] +
                    0.4 * pred_1m["confidence"], 2
                )
                strength = "CONFIRMED"

            if confidence < 0.45:  
                results.append(self.no_trade(asset, "Too weak"))
                continue

            bet = self.risk.calculate(confidence, pred_5m.get("rsi"))
            fb = self.feedback.evaluate(prediction)

            results.append({
                "asset": asset,
                "prediction": prediction,
                "confidence": confidence,
                "bet": bet,
                "accuracy": fb["accuracy"],
                "short_ma": pred_5m["short_ma"],
                "long_ma": pred_5m["long_ma"],
                "reason": f"{strength} | 1m({d1}) & 5m({d5})"
            })

        return results

    def no_trade(self, asset, reason):
        return {
            "asset": asset,
            "prediction": "NO TRADE",
            "confidence": 0,
            "bet": 0,
            "accuracy": None,
            "short_ma": None,
            "long_ma": None,
            "reason": reason
        }