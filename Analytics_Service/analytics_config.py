import os
from dotenv import load_dotenv

class AnalyticsConfig:
    def __init__(self):
        load_dotenv()
        self.bootstrap_servers = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'kafka:9092')
        self.topic_clean = os.getenv('TOPIC_CLEAN', 'clean')
        self.topic_analytics = os.getenv('TOPIC_ANALYTICS', 'analytics')


    def validate(self):
        if not self.bootstrap_servers.startswith('kafka:'):
            raise ValueError("KAFKA_BOOTSTRAP_SERVERS is missing!")
