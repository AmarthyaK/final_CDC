import sys

from src.config.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion
from src.exception import CustomException

from src.logger import logging

STAGE_NAME = "data_ingestion"

class DataIngestionPipeline:
    def __init__(self):
        pass
    def main(self):

        try:
            configmanager = ConfigurationManager()
            data_ingestion_config = configmanager.get_data_ingestion()
            data_ingestion = DataIngestion(data_ingestion_config)
            data_ingestion.download_data()
            data_ingestion.unzip_zip_files()
        except Exception as e:
            raise CustomException(e,sys)

if __name__ == "__main__":
    try:
        logging.info(f"stage name: {STAGE_NAME} has started")
        obj = DataIngestionPipeline()
        obj.main()
        logging.info(f"stage name: {STAGE_NAME} has completed")
        
    except Exception as e:
        raise CustomException(e,sys)