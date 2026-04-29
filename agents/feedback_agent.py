import random
from utils.logger import get_logger

logger = get_logger("FeedbackAgent")

class FeedbackAgent:
    def __init__(self):
        self.history = []

    def evaluate(self, prediction):
        try:
            actual = random.choice(["UP", "DOWN"])

            correct = prediction == actual
            self.history.append(correct)

            accuracy = sum(self.history) / len(self.history)

            logger.info(f"Actual: {actual}, Correct: {correct}, Accuracy: {round(accuracy,2)}")

            return {
                "actual": actual,
                "correct": correct,
                "accuracy": accuracy
            }

        except Exception as e:
            logger.error(f"Feedback error: {e}")
            return {}