import numpy as np
from utils.logger import get_logger

logger = get_logger("PredictionAgent")

class PredictionAgent:
    def predict(self, data):
        try:
            if len(data) < 20:
                raise ValueError("Not enough data")

            short = np.mean(data[-5:])
            long = np.mean(data[-20:])

            prediction = "UP" if short > long else "DOWN"
            confidence = 0.58

            logger.info(f"Prediction: {prediction}, Confidence: {confidence}")

            return {"prediction": prediction, "confidence": confidence}

        except Exception as e:
            logger.error(f"Prediction failed: {e}")
            return {"prediction": "NO TRADE", "confidence": 0}