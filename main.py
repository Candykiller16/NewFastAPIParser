import asyncio

import uvicorn

from src.di import container_general, container_parser, container_controller

# db = dao_container.db
#
# collection = db.lamoda

pylounge = {
    'title': "PyLounge",
    'url': 'https://www.youtube.com/watch?v=3bqcv8YmeQo&ab_channel=PyLounge-%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%D0%BD%D0%B0Python%D0%B8%D0%B2%D1%81%D1%91%D0%BEIT',
    'subscribers': 2100,
    'views': 900000
}

if __name__ == '__main__':
    # collection.drop()
    # ins_result = collection.insert_one(pylounge)
    # print(ins_result.inserted_id)
    # print(collection.count_documents({}))
    # pprint(asyncio.run(container_parser.lamoda.get_all_data()))

    # container_controller.lamoda.collection.drop()
    # container_controller.lamoda.collection.insert_one(pylounge)
    data = asyncio.run(container_parser.lamoda.get_all_data())
    for page in data:
        container_controller.lamoda.create_list(page)

    print(container_controller.lamoda.collection.count_documents({})) # 1500
    container_controller.lamoda.collection.drop()
    print(container_controller.lamoda.collection.count_documents({})) # 0
    uvicorn.run(
        container_general.app,
        host=container_general.config.service.host,
        port=container_general.config.service.port,
    )
