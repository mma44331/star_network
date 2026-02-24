import os
import gridfs
from pymongo import MongoClient

client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("MONGO_DB")]
fs = gridfs.GridFS(db)


class GridFSStorage:
    def __init__(self,mongo_uri, logger):
        self.mongo_uri = mongo_uri
        self.logger = logger

    def save(self,file_stream, image_id):
        content = file_stream.file.read()
        file_id = fs.put(content, filename=image_id)
        self.logger.info(f"Received {image_id}, size: {len(content)} bytes")
        return {"status": "success"}