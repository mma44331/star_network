from mongo_loader_config import MongoLoaderConfig
from fastapi import FastAPI, UploadFile, File
import uvicorn
from gridfsstorage import GridFSStorage
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("MONGO_LOADER")
config = MongoLoaderConfig()
app = FastAPI()
storage = GridFSStorage(config.mongo_uri,logger)

@app.post("/upload/{image_id}")
def upload(image_id: str, file: UploadFile = File(...)):
    success = storage.save(file,image_id)
    if success:
        logger.info(f"Successfully saved image {image_id} (Filename: {file.filename}) to GridFS")
        return {"status": "success", "image_id": image_id}
    else:
        logger.error(f"Failed to save image {image_id} to GridFS")
        return {"status": "error", "message": "Save failed"}, 500


if __name__ == "__main__":
    uvicorn.run("mongo_loader_orchestrator:app", host="localhost",port=8001 , reload=True)
