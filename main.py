import asyncio

import uvicorn

from src.di import container_general, container_parser, container_controller
from src.routers.lamoda import router as lamoda_router
# db = dao_container.db
#
# collection = db.lamoda

container_general.app.include_router(lamoda_router)

if __name__ == '__main__':
    # collection.drop()
    # ins_result = collection.insert_one(pylounge)
    # print(ins_result.inserted_id)
    # print(collection.count_documents({}))
    # pprint(asyncio.run(container_parser.lamoda.get_all_data()))

    # container_controller.lamoda.collection.drop()
    # container_controller.lamoda.collection.insert_one(pylounge)

    # data = asyncio.run(container_parser.lamoda.get_all_data())
    # for page in data:
    #     container_controller.lamoda.create_list(page)
    # print(container_controller.lamoda.collection.count_documents({})) # 1500
    # container_controller.lamoda.collection.drop()
    # print(container_controller.lamoda.collection.count_documents({})) # 0

    # data = asyncio.run(container_parser.lamoda.get_all_data())
    # for page in data:
    #     container_controller.lamoda.create_list(page)
    # print(container_controller.lamoda.get_list())

    uvicorn.run(
        container_general.app,
        host=container_general.config.service.host,
        port=container_general.config.service.port,
    )
