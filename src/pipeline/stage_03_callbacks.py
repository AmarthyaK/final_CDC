## Pipeline

from src.exception import CustomException

from src.config.configuration import ConfigurationManager
from src.components.callbacks import PrepareCallbacks

import sys

class CallbacksPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            configmanager = ConfigurationManager()
            prepare_callbacks_config = configmanager.prepare_callbacks()
            prepare_callbacks = PrepareCallbacks(prepare_callbacks_config)
            callbacks_list = prepare_callbacks.get_tb_ckpt_callbacks()

        except Exception as e:
            raise CustomException(e,sys)