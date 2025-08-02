import os 
import tensorflow as tf
from Classifier.entity.config_entity import EvaluationConfig
from Classifier.utils.utilities import save_json
from pathlib import Path

class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config
    
    def _valid_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split = 0.2,  # 20% for validation
        )
        dataflow_kwargs = dict(
            target_size = self.config.params_image_size[:-1],
            batch_size = self.config.params_batch_size,
            interpolation = "bilinear",
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory = self.config.training_data,
            subset = "validation",
            class_mode = "sparse",
            shuffle = False,
            **dataflow_kwargs
        )
      
    @staticmethod
    def load_model(path : Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)
    
    def evaluate_model(self):
        self.model = self.load_model(self.config.path_of_model)
        self.model.compile(
            loss='sparse_categorical_crossentropy',
            optimizer=tf.keras.optimizers.SGD(learning_rate=self.config.params_learning_rate),
            metrics=['accuracy']
        )
        self._valid_generator()
        self.score = self.model.evaluate(
            self.valid_generator,
        )

    def save_score(self):
        score = {
            "loss": self.score[0],
            "accuracy": self.score[1]
        }
        save_json(path=Path("scores.json"),data=score)
        print(f"Model evaluation score: {score}")
    

