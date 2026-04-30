import numpy as np
import random
from utils.logger import get_logger

logger = get_logger("PredictionAgent")

class PredictionAgent:

    def compute_rsi(self, data, period=14):
        deltas = np.diff(data)
        gains = np.where(deltas > 0, deltas, 0)
        losses = np.where(deltas < 0, -deltas, 0)

        avg_gain = np.mean(gains[-period:])
        avg_loss = np.mean(losses[-period:])

        if avg_loss == 0:
            return 100

        rs = avg_gain / avg_loss
        return 100 - (100 / (1 + rs))

    def compute_adx(self, data, period=14):
        diffs = np.diff(data)
        up = np.where(diffs > 0, diffs, 0)
        down = np.where(diffs < 0, -diffs, 0)

        avg_up = np.mean(up[-period:])
        avg_down = np.mean(down[-period:])

        if avg_up + avg_down == 0:
            return 0

        dx = abs(avg_up - avg_down) / (avg_up + avg_down)
        return dx * 100

    def predict(self, data):
        try:
            if len(data) < 30:
                raise ValueError("Not enough data")

            short = float(np.mean(data[-5:]))
            long = float(np.mean(data[-20:]))

            momentum = (data[-1] - data[-6]) / data[-6]
            rsi = self.compute_rsi(data)
            adx = self.compute_adx(data)

            diff = abs(short - long) / long

       
            if adx < 5:
                logger.info(f"SIDEWAYS (ADX {round(adx,2)}) → NO TRADE")
                return self.no_trade(short, long)

            prediction = "UP" if short > long else "DOWN"

         
            confidence = (
                0.4
                + 4 * diff
                + 2 * abs(momentum)
                + (adx / 120)
            )

           
            confidence += random.uniform(-0.02, 0.02)

         
            confidence = max(0.3, min(confidence, 0.9))
            confidence = round(confidence, 2)

            logger.info(
                f"{prediction} | Conf: {confidence} | ADX: {round(adx,2)} | RSI: {round(rsi,2)}"
            )

            return {
                "prediction": prediction,
                "confidence": confidence,
                "short_ma": short,
                "long_ma": long,
                "rsi": rsi,
                "adx": adx
            }

        except Exception as e:
            logger.error(f"Prediction failed: {e}")
            return self.no_trade(None, None)

    def no_trade(self, short, long):
        return {
            "prediction": "NO TRADE",
            "confidence": 0,
            "short_ma": short,
            "long_ma": long,
            "rsi": None,
            "adx": None
        }