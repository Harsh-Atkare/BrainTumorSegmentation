from src.BrainTumorReport import logger
from src.BrainTumorReport.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME="Data Ingestion Stage"
try:
    logger.info(f'>>>>>> stage 1 {STAGE_NAME} Started<<<<<<')
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'>>>>>> Stage 1 {STAGE_NAME} Completed')
except Exception as e:
    logger.exception(e)
    raise e