from utils.logger import get_logger

logger = get_logger("RiskAgent")

class RiskAgent:
    def calculate(self, confidence, rsi=None):
        try:
            if confidence <= 0 or confidence >= 1:
                return 0

            f = confidence * (confidence - (1 - confidence))
            f *= confidence

        
            if confidence < 0.65:
                f *= 0.6

     
            if rsi and (rsi < 30 or rsi > 70):
                f *= 0.5

            f = max(0, min(f, 0.1))

            logger.info(f"Calculated bet size: {round(f,4)}")
            return f

        except Exception as e:
            logger.error(f"Risk error: {e}")
            return 0