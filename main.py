import asyncio
from json import dumps, loads

import uvicorn
from kafka import KafkaProducer, KafkaConsumer

from src.di import container_general, container_parser, container_controller
from src.routers.lamoda import router as lamoda_router
from src.routers.twitch import router as twitch_router


container_general.app.include_router(lamoda_router)
container_general.app.include_router(twitch_router)

if __name__ == '__main__':
    container_controller.lamoda.drop_collection()

    data = asyncio.run(container_parser.lamoda.get_all_data())
    for page in data:
        container_controller.lamoda.insert_sneaker_to_mongo(page)
    print(container_controller.lamoda.count_documents())  # 1566

    producer = KafkaProducer(
        retries=5,
        api_version=(0, 11, 5),
        bootstrap_servers=["kafka:9092"],
        value_serializer=lambda x: dumps(x).encode("utf-8"),
    )
    consumer = KafkaConsumer(
        "topictwitch",
        api_version=(0, 11, 5),
        bootstrap_servers=["kafka:9092"],
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        consumer_timeout_ms=2000,
        heartbeat_interval_ms=200,
        group_id="1",
        value_deserializer=lambda x: loads(x.decode("utf-8")),
    )
    consumer.subscribe(topics=["topictwitch"])
    data = container_parser.twitch.get_data_from_twich_api()
    for stream_data in data:
        producer.send("topictwitch", value=stream_data)
        print(f"{stream_data} product inserted!")
    print("Items send")

    list_of_data = []
    for message in consumer:
        list_of_data.append(message.value)
    container_controller.twitch.insert_streams_to_mongo(streams=list_of_data)
    print(container_controller.twitch.count_documents())
    uvicorn.run(
        "src.di:container_general.app",
        host=container_general.config.service.host,
        port=container_general.config.service.port,
        reload=True,
    )
