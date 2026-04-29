from dotenv import load_dotenv
load_dotenv()

from agents.search_agent import SearchAgent
from agents.data_agent import DataAgent
from agents.prediction_agent import PredictionAgent
from agents.risk_agent import RiskAgent
from agents.feedback_agent import FeedbackAgent
from agents.hermes_controller import HermesController
from utils.logger import get_logger
from utils.apify_client import ApifyClientWrapper
from utils.llm_client import LLMClient

logger = get_logger("Main")

def main():
    try:
        search = SearchAgent()
        data_agent = DataAgent()
        predictor = PredictionAgent()
        risk = RiskAgent()
        feedback = FeedbackAgent()
        apify = ApifyClientWrapper()
        llm = LLMClient()

        # Apify check
        try:
            run_id = apify.test_run()
            logger.info(f"Apify working: {run_id}")
        except Exception as e:
            logger.warning(f"Apify failed: {e}")

        controller = HermesController(
            search, data_agent, predictor, risk, feedback
        )

        results = controller.run()

        print("\nASSET | PRED | CONF | BET")

        for r in results:
            print(f"{r['asset']} | {r['prediction']} | {r['confidence']} | {round(r['bet']*100,2)}%")
            llm.explain(r["prediction"], r["confidence"])

        logger.info("Pipeline completed")

    except Exception as e:
        logger.critical(f"System failure: {e}")

if __name__ == "__main__":
    main()