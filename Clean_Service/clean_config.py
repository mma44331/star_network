import json
import os
import time
from dotenv import load_dotenv
from confluent_kafka import Consumer, KafkaError

load_dotenv()



import os
from dotenv import load_dotenv

class CleanConfig:
    def __init__(self):
        load_dotenv()
        self.bootstrap_servers = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'kafka:9092')
        self.topic_rae = os.getenv('TOPIC_RAW', 'rae')
        self.topic_clean = os.getenv('TOPIC_CLEAN', 'clean')

    def validate(self):
        if not self.bootstrap_servers.startswith('kafka:'):
            raise

