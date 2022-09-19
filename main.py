import uvicorn
from pymongo import MongoClient

from src.di import container_general

db_client = MongoClient(
    "mongodb://mongodb:27017/?authSource=admin&readPreference=secondary&directConnection=true&ssl=false",
    username="mongoadmin", password="mongopassword"
)

db = db_client["test_data"]

collection = db["test_collection"]

if __name__ == '__main__':
    print(collection.count_documents({}))
    uvicorn.run(
        container_general.app,
        host=container_general.config.service.host,
        port=container_general.config.service.port,
    )
