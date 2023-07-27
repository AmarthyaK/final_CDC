from src.entity.config_entity import DataIngestionConfig
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
