import os
from dotenv import load_dotenv

class MongoLoaderConfig:
    def __init__(self):
        load_dotenv()
        self.mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017')
        self.db_name = os.getenv('MONGO_DB', 'correspondents_network')
    def validate(self):
        if not self.mongo_uri.startswith('mongodb://'):
            raise ValueError(f"Invalid MONGO_URI: {self.mongo_uri}. Must start with 'mongodb://'")