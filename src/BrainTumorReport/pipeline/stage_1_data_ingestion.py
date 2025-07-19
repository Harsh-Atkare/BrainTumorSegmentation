from BrainTumorReport.config.configuration import ConfigurationManager
from BrainTumorReport.components.data_ingestion import DataIngestion
from BrainTumorReport import logger
STAGE_NAME="Data Ingestion Stage"
class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config=ConfigurationManager()
        DataIngestionConfig=config.get_data_ingestion_config()
        dataIngestion=DataIngestion(config=DataIngestionConfig)
        dataIngestion.download_file()
        dataIngestion.extract_zip_file()
        dataIngestion.delete_zip_file()

if __name__ =='__main__':
    try:
        logger.info(f'>>>>>> stage 1 {STAGE_NAME} Started<<<<<<')
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f'>>>>>> Stage 1 {STAGE_NAME} Completed')
    except Exception as e:
        logger.exception(e)
        raise e