from CNN_based_disease_classifier import logger
from CNN_based_disease_classifier.pipeline.step_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion Step"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

