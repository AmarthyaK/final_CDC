from src.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.logger import logging
from src.exception import CustomException
import sys

STAGE_NAME = "DataIngestionPipeline"

try:
    logging.info(f"stage name: {STAGE_NAME} has started")
    obj = DataIngestionPipeline()
    obj.main()
    logging.info(f"stage name: {STAGE_NAME} has completed")
    
except Exception as e:
    raise CustomException(e,sys)