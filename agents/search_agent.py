from utils.logger import get_logger

logger = get_logger("SearchAgent")

class SearchAgent:
    def __init__(self):
        self.markets = ["BTC", "ETH"]

    def run(self) -> list:
        try:
            logger.info("Identifying crypto markets...")
            return self.markets
        except Exception as e:
            logger.error(f"Failed to identify markets: {e}")
            return []