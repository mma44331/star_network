import os

import logging

from clean_config import CleanConfig
from clean_orchestrator import CleanOrchestrator
from kafka_publisher import KafkaPublisher
from kafka_consumer import KafkaConsumer
from text_cleaner import TextCleaner
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("CLEAN_SERVICE")


config = CleanConfig()
group_id = f"{config.topic_rae}_raw"
publisher = KafkaPublisher(config.bootstrap_servers,config.topic_clean,logger)
consumer = KafkaConsumer(config.bootstrap_servers,config.topic_rae,group_id,logger)
cleaner = TextCleaner(logger)
orchestrator = CleanOrchestrator(consumer,cleaner,publisher,logger)


def main():
    orchestrator.run()

if __name__ == "__main__":
    main()

