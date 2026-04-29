import requests
import os
from utils.logger import get_logger

logger = get_logger("LLM")

class LLMClient:
    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")

    def explain(self, prediction, confidence):
        try:
            if not self.api_key:
                logger.warning("No OpenRouter key")
                return None

            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json",
                    "HTTP-Referer": "http://localhost",  
                    "X-Title": "crypto-agent"
                },
                json={
                    "model": "openai/gpt-3.5-turbo", 
                    "messages": [
                        {
                            "role": "user",
                            "content": f"Explain why prediction is {prediction} with confidence {confidence}"
                        }
                    ]
                },
                timeout=15
            )

            response.raise_for_status()

            data = response.json()
            logger.info("LLM success")

            return data["choices"][0]["message"]["content"]

        except Exception as e:
            logger.error(f"LLM error: {e}")
            return None