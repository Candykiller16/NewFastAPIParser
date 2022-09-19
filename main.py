import uvicorn

from src.di import container_general, dao_container

db = dao_container.db

collection = db.lamoda

pylounge = {
    'title': "PyLounge",
    'url': 'https://www.youtube.com/watch?v=3bqcv8YmeQo&ab_channel=PyLounge-%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%D0%BD%D0%B0Python%D0%B8%D0%B2%D1%81%D1%91%D0%BEIT',
    'subscribers': 2100,
    'views': 900000
}

if __name__ == '__main__':
    # collection.drop()
    ins_result = collection.insert_one(pylounge)
    print(ins_result.inserted_id)
    print(collection.count_documents({}))
    uvicorn.run(
        container_general.app,
        host=container_general.config.service.host,
        port=container_general.config.service.port,
    )
