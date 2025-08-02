#Components
import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf 
import time 
import logging
from Classifier.entity.config_entity import PrepareCallbacksConfig
class PrepareCallbacks:
    def __init__(self, config: PrepareCallbacksConfig):
        self.config = config
    
    @property
    def _create_tb_callbacks(self):
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        tb_running_log_dir = os.path.join(
            self.config.tensorboard_root_log_dir, 
            f"tb_logs_at-{timestamp}"
        )
        logging.info(f"Tensorboard log dir: {tb_running_log_dir}")
        return tf.keras.callbacks.TensorBoard(
            log_dir=tb_running_log_dir,
            histogram_freq=1, #Problem might occur 
            write_graph=True,  
            write_images=True,
            update_freq="epoch",
        )
    
    @property
    def _create_checkpoint_callback(self):
        logging.info(f"Checkpoint dir: --->>>>> creating checkpoint dir ----->")
        return tf.keras.callbacks.ModelCheckpoint(
            filepath = self.config.checkpoint_model_path,
            monitor = "val_accuracy", #problems might occur 
            save_best_only = True,
        )
    
    def get_callbacks(self):
        logging.info("Preparing callbacks")
        return [
            self._create_tb_callbacks,
            self._create_checkpoint_callback
        ]
         
        