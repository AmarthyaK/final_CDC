import os
from src.utils.common import download_zip_files
from src.utils.common import unzip_zip_files
from src.utils.common import download_s3
from src.entity.config_entity import DataIngestionConfig


from src.logger import logging


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_data(self):
        """
        Download data from S3
        """
        download_s3(self.config.local_data_file)
    def unzip_zip_files(self):
        """Unzipping files"""
        unzip_zip_files(self.config.local_data_file,self.config.unzip_dir)
