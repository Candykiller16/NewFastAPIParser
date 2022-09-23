from json import loads, dumps

from kafka import KafkaConsumer, KafkaProducer


class Kafka:
    def __init__(self):
        self.producer = KafkaProducer(
            retries=5,
            bootstrap_servers=["kafka:9092"],
            api_version=(0, 11, 5),
            value_serializer=lambda x: dumps(x).encode("utf-8"),
        )
        self.consumer_twitch = KafkaConsumer(
            "topic_twitch",
            bootstrap_servers=["kafka:9092"],
            auto_offset_reset="earliest",
            enable_auto_commit=True,
            consumer_timeout_ms=2000,
            heartbeat_interval_ms=200,
            group_id="2",
            value_deserializer=lambda x: loads(x.decode("utf-8")),
        )
        self.consumer_twitch.subscribe(topics=["topic_twitch"])
