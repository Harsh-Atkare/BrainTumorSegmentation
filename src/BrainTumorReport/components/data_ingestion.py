# components
import os
import urllib.request as request
import zipfile
import gdown
from src.BrainTumorReport import logger
from src.BrainTumorReport.utils.common import get_size
from BrainTumorReport.entity.config_entity import DataIngestionConfig
# main logic code
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self)->str:

        try:
            dataset_url = self.config.source_URL
            zip_doownload_dir=self.config.local_data_file
            os.makedirs("artifacts/data_ingestion",exist_ok=True)
            logger.info(f"Downloading file from {dataset_url} into file  {zip_doownload_dir}")


            file_id=dataset_url.split('/')[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id,zip_doownload_dir)
            logger.info(f"File Downloaded at {zip_doownload_dir}")

        except Exception as e:
            raise e
    
    def extract_zip_file(self):
        unzip_dir=self.config.unzip_dir
        os.makedirs(unzip_dir,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_dir)
        logger.info(f"Unzipped file at {unzip_dir}")

    def delete_zip_file(self):
        os.remove(self.config.local_data_file)
        logger.info(f"Deleted zip file at {self.config.local_data_file}")
    