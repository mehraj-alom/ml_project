from Classifier.entity.config_entity import TrainingConfig
import tensorflow as tf
from pathlib import Path
from Classifier import logger

class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config
        
    def get_base_model(self):
        self.model = tf.keras.models.load_model(self.config.updated_base_model_path)
   
    # ✅ Recompile the model with a new optimizer instance
        self.model.compile(
            loss='sparse_categorical_crossentropy',
            optimizer=tf.keras.optimizers.SGD(),
             metrics=['accuracy']
         )

        logger.info(f"Base model loaded and recompiled from {self.config.updated_base_model_path}")

    def train_valid_generator(self):

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

        if self.config.params_is_augmentation:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range = 40,
                width_shift_range = 0.2,
                height_shift_range = 0.2,
                shear_range = 0.2,
                zoom_range = 0.2,
                horizontal_flip = True,
                fill_mode = "nearest",
                **datagenerator_kwargs
            )
        else:
            train_datagenerator = valid_datagenerator
        

        self.train_generator = train_datagenerator.flow_from_directory(
            directory = self.config.training_data,
            subset = "training",
            class_mode = "sparse",
            shuffle = True,
            **dataflow_kwargs
        )

    @staticmethod
    def save_model(path :Path, model: tf.keras.Model):
        logger.info(f"Saving model at {path}")
        model.save(path)
    
    def train(self, callback_List :list):
        logger.info("Training started")
        self.steps_per_epoch = self.train_generator.samples // self.config.params_batch_size
        self.validation_steps = self.valid_generator.samples // self.config.params_batch_size
        
        self.model.fit(
            self.train_generator,
            steps_per_epoch = self.steps_per_epoch,
            validation_data = self.valid_generator,
            validation_steps = self.validation_steps,
            epochs = self.config.params_epochs,
            callbacks = callback_List
        )

        self.save_model(
            path = self.config.trained_model_path,
            model = self.model
        )