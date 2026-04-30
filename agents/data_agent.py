import requests
from utils.logger import get_logger

logger = get_logger("DataAgent")

class DataAgent:
    def fetch_data(self, asset, interval="1m"):
        try:
            logger.info(f"Fetching {interval} data for {asset}")

            url = "https://api.binance.com/api/v3/klines"
            params = {
                "symbol": f"{asset}USDT",
                "interval": interval,
                "limit": 100
            }

            res = requests.get(url, params=params, timeout=10)

            if res.status_code != 200:
                raise ValueError(f"Bad response: {res.status_code}")

            data = res.json()

            if not data:
                raise ValueError("Empty data received")

            closes = [float(x[4]) for x in data]

            logger.info(f"Fetched {len(closes)} {interval} candles for {asset}")
            return closes

        except requests.exceptions.Timeout:
            logger.error(f"Timeout while fetching {asset} ({interval})")

        except requests.exceptions.RequestException as e:
            logger.error(f"Request error: {e}")

        except Exception as e:
            logger.error(f"Unexpected error: {e}")

        return []