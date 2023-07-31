## Pipeline

from src.exception import CustomException

from src.config.configuration import ConfigurationManager

from src.components.callbacks import PrepareCallbacks
from src.components.model_training import Training


import sys

class Callbacks_ModelTrain_Pipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            configmanager = ConfigurationManager()
            prepare_callbacks_config = configmanager.prepare_callbacks()
            prepare_callbacks = PrepareCallbacks(prepare_callbacks_config)
            callbacks_list = prepare_callbacks.get_tb_ckpt_callbacks()

            #training model
            model_train_config = configmanager.model_train_config()
            model_train = Training(model_train_config)
            model_train.get_base_model()
            model_train.train_valid_generator()
            model_train.train(callbacks_list)

        except Exception as e:
            raise CustomException(e,sys)