import os 
from urllib import request 
from zipfile import ZipFile
from Classifier import logger
from Classifier.utils.utilities import get_size
from Classifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            logger.info(f"Downloading file from {self.config.source_URL} to {self.config.local_data_file}")
            filename , headers = request.urlretrieve(
                url = self.config.source_URL, 
                filename = self.config.local_data_file)
            logger.info(f"File downloaded: {filename}")
            
        else:
            logger.info(f"File already exists: {self.config.local_data_file}")   

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with ZipFile(self.config.local_data_file, 'r') as zip_ref:
            logger.info(f"Extracting zip file to {unzip_path}")
            zip_ref.extractall(unzip_path)
            logger.info(f"Zip file extracted to {unzip_path}")