
from Classifier import logger
from Classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from Classifier.pipeline.stage_03_training import ModelTrainingPipeline
from Classifier.pipeline.stage_04_evaluation import EvaluationPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare Base Model stage"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Training"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "EVALUATION "

try:
    logger.info(f"------------------->>>>")
    logger.info(f"===>> {STAGE_NAME} has started ==>")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f"=======>>>> {STAGE_NAME} has Completed <<<<<<<=====")
except Exception as e:
    logger.info(e)
    raise e