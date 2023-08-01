from src.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
from src.pipeline.stage_03_callbacks_model_training import Callbacks_ModelTrain_Pipeline
from src.pipeline.stage_04_evaluation import Evaluationpipeline


from src.logger import logging
from src.exception import CustomException
import sys

STAGE_NAME = "DataIngestionPipeline"

try:
    #Data_ingestion
    logging.info(f"stage name: {STAGE_NAME} has started")
    obj = DataIngestionPipeline()
    obj.main()
    logging.info(f"stage name: {STAGE_NAME} has completed")
    
except Exception as e:
    raise CustomException(e,sys)

STAGE_NAME = "Prepare_base_model"

try:
    #Prepare_base_model
    logging.info(f"stage name: {STAGE_NAME} has started")
    obj = PrepareBaseModelPipeline()
    obj.main()
    logging.info(f"stage name: {STAGE_NAME} has completed")
    
except Exception as e:
    raise CustomException(e,sys)

STAGE_NAME = "Callbacks and Model Training"

try:
    #Prepare_base_model
    logging.info(f"stage name: {STAGE_NAME} has started")
    obj = Callbacks_ModelTrain_Pipeline()
    obj.main()
    logging.info(f"stage name: {STAGE_NAME} has completed")
    
except Exception as e:
    raise CustomException(e,sys)


STAGE_NAME = "Evaluation"

try:
    #Prepare_base_model
    logging.info(f"stage name: {STAGE_NAME} has started")
    obj = Evaluationpipeline()
    obj.main()
    logging.info(f"stage name: {STAGE_NAME} has completed")
    
except Exception as e:
    raise CustomException(e,sys)