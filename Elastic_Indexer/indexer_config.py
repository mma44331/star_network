import os
from elasticsearch import Elasticsearch
from dotenv import load_dotenv


class IndexerConfig:
    def __init__(self):
        load_dotenv()
        self.bootstrap_servers = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'kafka:9092')
        self.topics = [os.getenv('TOPIC_RAW', 'raw'),os.getenv('TOPIC_CLEAN', 'clean'),os.getenv('TOPIC_ANALYTICS', 'analytics')]
        self.es = Elasticsearch(os.getenv('HOST_ELASTICSEARCH'),basic_auth=("elastic", "JcLN00crDrsRsawPFRM*"),verify_certs=False)


    def validate(self):
        if not self.bootstrap_servers.startswith('kafka:'):
            raise ValueError("KAFKA_BOOTSTRAP_SERVERS is missing!")
