import requests

class MongoLoaderClient:
    def __init__(self, mongo_loader_url, logger):
        self.url = mongo_loader_url
        self.logger = logger

    def send(self, file_path, image_id):
        self.logger.info(f"Sending {image_id} to MongoDB Loader")
        with open(file_path, "rb") as f:
            response = requests.post(f"{self.url}/upload/{image_id}", files={"file": f})
        return response.status_code == 200 