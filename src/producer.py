from kafka import KafkaProducer
import pandas as pd
import json
from config import Config

def kafka_producer():
    producer = KafkaProducer(
        bootstrap_servers=Config.KAFKA_BROKER_URL,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    df = pd.read_csv(Config.IMDB_DATASET_PATH)

    for _, row in df.iterrows():
        producer.send(Config.KAFKA_TOPIC, value=row.to_dict())
    
    producer.flush()
    print(f"Sent {len(df)} rows to Kafka topic '{Config.KAFKA_TOPIC}'.")

if __name__ == "__main__":
    kafka_producer()

