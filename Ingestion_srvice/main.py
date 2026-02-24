import logging
import os
import uvicorn
from fastapi import FastAPI
from ingestion_config import IngestionConfig
from ocr_engine import OCREngine
from metadata_extractor import MetadataExtractor
from mongo_loader_client import MongoLoaderClient
from ingestion_orchestrator import IngestionOrchestrator
from kafka_publisher import Kafkapublisher
from dotenv import load_dotenv
load_dotenv()
path_from_config = os.getenv("TESSERACT_PATH")

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("INGESTION_SERVICE")
config = IngestionConfig()
ocr_engine = OCREngine(path_from_config,logger)
metadata_extractor = MetadataExtractor(logger)
mongo_client = MongoLoaderClient(config.mongo_loader_url, logger)
kafka = Kafkapublisher(config.kafka_bootstrap_servers,config.topic_raw,logger)

orchestrator = IngestionOrchestrator(
    config=config,
    ocr_engine=ocr_engine,
    metadata_extractor=metadata_extractor,
    mongo_client=mongo_client,
    kafka=kafka,
    logger=logger
)
@app.get('/process')
def process_all():
    orchestrator.run()
    return {"status": "Ingestion process completed. Check logs for details."}


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost",port=8000 , reload=True)
