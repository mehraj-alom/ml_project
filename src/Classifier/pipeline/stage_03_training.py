from Classifier.config.configuration import ConfigurationManager
from Classifier.components.prepare_callbacks import  PrepareCallbacks
from Classifier.components.training import Training
from Classifier import logger   

STAGE_NAME = "Training Stage"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callbacks_config()
        prepare_callbacks = PrepareCallbacks(config=prepare_callbacks_config)
        callbacks = prepare_callbacks.get_callbacks()
        logger.info(f"Callbacks: {callbacks}")

        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callback_List=callbacks
        )


if __name__ == "__main__":
    try:
        logger.info(f"{STAGE_NAME} started")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} completed")
    except Exception as e:
        logger.exception(f"{STAGE_NAME} failed with exception: {e}")
        raise e
