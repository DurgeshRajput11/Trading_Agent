from apify_client import ApifyClient
import os

class ApifyClientWrapper:
    def __init__(self):
        token = os.getenv("APIFY_TOKEN")
        if not token:
            raise ValueError("APIFY_TOKEN missing")

        self.client = ApifyClient(token)

    def test_run(self):
        run = self.client.actor("apify/hello-world").call(
            run_input={"message": "Hello from Python"}
        )
        return run["id"]