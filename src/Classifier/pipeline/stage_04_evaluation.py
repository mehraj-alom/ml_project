from Classifier.config.configuration import ConfigurationManager
from Classifier.components.evaluation import Evaluation
from Classifier import logger

STAGE_NAME = "Evaluation Stage"

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_evaluation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluate_model()
        evaluation.save_score()


if __name__ == "__main__":
    try:
        logger.info(f"------------------->>>>")
        logger.info(f"===>> {STAGE_NAME} has started ==>")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f"=======>>>> {STAGE_NAME} has Completed <<<<<<<=====")
    except Exception as e:
        logger.info(e)
        raise e