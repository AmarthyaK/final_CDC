from src.config.configuration import ConfigurationManager
from src.components.evaluation import Evaluation
from src.logger import logging

from src.exception import CustomException
import sys

class Evaluationpipeline:
    def __init__(self):
        pass
    def main(self):
        

        configmanager = ConfigurationManager()
        eval_config = configmanager.get_validation_config()
        evaluation_class = Evaluation(eval_config)

        logging.info(f"{eval_config}")

        evaluation_class.evaluation_method()
        logging.info("Evaluation pipeline completed")
        logging.info("Saving score")
        evaluation_class.save_score()