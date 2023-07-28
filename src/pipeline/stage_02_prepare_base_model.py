from src.config.configuration import ConfigurationManager
from src.components.prepare_base_model import PrepareBaseModel
from src.logger import logging

import sys
from src.exception import CustomException

STAGE_NAME = "prepare_base_model_pipeline"


class PrepareBaseModelPipeline:
    def __init__(self):
        pass
    def main(self):
        ## Pipeline

        try:
            configmanager = ConfigurationManager()
            prepare_base_model_config = configmanager.prepare_base_model()
            prepare_base_model = PrepareBaseModel(prepare_base_model_config)
            prepare_base_model.download_base_model()
            prepare_base_model.update_base_model()

        except Exception as e:
            raise CustomException(e,sys)

