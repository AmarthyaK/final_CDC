from src.entity.config_entity import DataIngestionConfig
from src.entity.config_entity import BaseModelConfig
from src.entity.config_entity import PrepareCallbacksConfig
from src.entity.config_entity import ModelTrainConfig

import os
from pathlib import Path

from src.utils.common import create_directories
from src.utils.common import read_yaml
from src.constants import constant_paths

from src.logger import logging

CONFIG_FILE_PATH = constant_paths().get_paths()[0]
PARAMS_FILE_PATH = constant_paths().get_paths()[1]

#creating a class called Configuration manager
#also reading yaml files (config and params)
#read_yaml's output is a dictionary type datatype called ConfigBox

class ConfigurationManager:
    def __init__(
            self,
            config_file_path = CONFIG_FILE_PATH,
            params_file_path = PARAMS_FILE_PATH):
        
        logging.info("reading yaml files started")
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        logging.info("reading yaml files finished")

        create_directories([self.config.artifacts_dir])
        logging.info("Artifacts directory created successfully")

    def get_data_ingestion(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        Data_ingestion_Config = DataIngestionConfig(root_dir=config.root_dir,source_URL=config.source_URL,
                                                    local_data_file=config.local_data_file,unzip_dir=config.unzip_dir)
        #returning a class with loaded data path files
        return Data_ingestion_Config

    def prepare_base_model(self) -> BaseModelConfig:
            config = self.config.base_model

            create_directories([config.root_dir])

            base_model_config = BaseModelConfig(
                root_dir = config.root_dir,
                base_model_path=config.base_model_path,
                updated_base_model_path= config.updated_base_model_path,
                params_img_size=self.params.IMAGE_SIZE,
                params_batch_size=self.params.BATCH_SIZE,
                params_include_top=self.params.INCLUDE_TOP,
                params_learning_rate=self.params.LEARNING_RATE,
                params_epochs=self.params.EPOCHS,
                params_weights=self.params.WEIGHTS,
                params_classes=self.params.CLASSES
            )
            #returning a class with loaded data path files
            return base_model_config
    
    def prepare_callbacks(self) -> PrepareCallbacksConfig:
        config = self.config.prepare_callbacks
        create_directories([config.root_dir])

        model_checkpoint_dir = os.path.dirname(config.checkpoint_model_file_path)

        create_directories([Path(model_checkpoint_dir),Path(config.tensorboard_root_log_dir)])

        prepare_callbacks_config = PrepareCallbacksConfig(
            root_dir = Path(config.root_dir),
            tensorboard_root_log_dir=Path(config.tensorboard_root_log_dir),
            checkpoint_model_file_path= Path(config.checkpoint_model_file_path)
        )
        #returning a class with loaded data path files
        return prepare_callbacks_config

    def model_train_config(self) -> ModelTrainConfig:
        training = self.config.model_train
        prepare_base_model = self.config.base_model
        params = self.params
        training_data_path = os.path.join(self.config.data_ingestion.unzip_dir,"Dataset_CDC_category")
        create_directories([Path(training.root_dir)])

        model_train_config = ModelTrainConfig(
            root_dir = Path(training.root_dir),
            trained_model_path = Path(training.trained_model_path),
            updated_base_model_path=self.config.base_model.updated_base_model_path,
            training_data=Path(training_data_path),
            params_epochs = params.EPOCHS,
            params_batch_size = params.BATCH_SIZE,
            params_image_size = params.IMAGE_SIZE,
            params_is_augmentation= params.AUGMENTATION
        )

        return model_train_config