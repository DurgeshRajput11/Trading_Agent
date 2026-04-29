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
            data = self.data.fetch_data(asset)

            if not data:
                continue

            pred = self.predictor.predict(data)

            if pred["confidence"] < 0.55:
                continue

            bet = self.risk.calculate(pred["confidence"])
            fb = self.feedback.evaluate(pred["prediction"])

            results.append({
                "asset": asset,
                "prediction": pred["prediction"],
                "confidence": pred["confidence"],
                "bet": bet,
                "accuracy": fb["accuracy"]
            })

        return results