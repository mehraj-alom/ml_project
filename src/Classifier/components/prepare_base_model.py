#components
import os 
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
from Classifier.entity.config_entity import PrepareBaseModelConfig
from pathlib import Path

class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config
    
    def get_base_model(self):
        self.model = tf.keras.applications.vgg16.VGG16(
            input_shape = self.config.params_image_size,
            weights = self.config.params_weights,
            include_top = self.config.params_include_top,
        )
        self.save_model(path=self.config.base_model_path,model=self.model)

    @staticmethod  #Belongs to the class logically but doesn't need the class or instance state to do its job.
    def _prepare_full_model(model,classes,freeze_all,freeze_till,Learning_rate):
        if freeze_all:
            for layer in model.layers:
                layer.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:freeze_till]:
                layer.trainable = False     
        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(
            units = classes,
            activation = 'softmax',
        )(flatten_in) #flattens everything in 1D

        full_model = tf.keras.models.Model(
            inputs = model.input,
            outputs = prediction
        )
        full_model.compile(
            loss = 'sparse_categorical_crossentropy',
            optimizer = tf.keras.optimizers.SGD(learning_rate=Learning_rate),
            metrics = ['accuracy']
        )

        full_model.summary()
        return full_model

    def update_base_model(self):
        self.model = self._prepare_full_model(
            model=self.model,
            classes=self.config.params_classes,
            freeze_all=True,
            freeze_till=None,
            Learning_rate=self.config.params_learning_rate
        )
        self.save_model(path=self.config.updated_model_path,model=self.model)
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)
        print(f"Model saved at {path}")
    