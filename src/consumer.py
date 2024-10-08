from kafka import KafkaConsumer
import json
from config import Config
from s3_utils import upload_to_s3

def kafka_consumer():
    consumer = KafkaConsumer(
        Config.KAFKA_TOPIC,
        bootstrap_servers=Config.KAFKA_BROKER_URL,
        value_deserializer=lambda v: json.loads(v.decode('utf-8'))
    )

    for message in consumer:
        data = message.value
        # Here you can apply transformations if necessary
        upload_to_s3(data)

if __name__ == "__main__":
    kafka_consumer()

