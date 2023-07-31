from src.config.configuration import ConfigurationManager
from src.components.evaluation import Evaluation

from src.exception import CustomException
import sys

class Evaluationpipeline:
    def __init__(self):
        pass
    def main(self):

        try:
            configmanager = ConfigurationManager()
            eval_config = configmanager.get_validation_config()
            evaluation = Evaluation(eval_config)
            evaluation.evaluation()
            evaluation.save_score()

        except Exception as e:
            CustomException(e,sys)