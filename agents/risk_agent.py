from utils.logger import get_logger

logger = get_logger("RiskAgent")

class RiskAgent:
    def calculate(self, confidence):
        try:
            if confidence <= 0 or confidence >= 1:
                raise ValueError("Invalid confidence")

            p = confidence
            q = 1 - p
            b = 1

            f = (b * p - q) / b
            f = max(0, min(f, 0.2))

            logger.info(f"Calculated bet size: {round(f,4)}")
            return f

        except Exception as e:
            logger.error(f"Risk calculation failed: {e}")
            return 0