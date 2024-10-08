import os

class Config:
    # AWS Configurations
    AWS_REGION = os.getenv('AWS_REGION', 'us-east-1')

    # MSK Configurations
    MSK_CLUSTER_NAME = os.getenv('MSK_CLUSTER_NAME', 'imdb-cluster')
    KAFKA_BROKER_URL = os.getenv('KAFKA_BROKER_URL', 'your-msk-broker-url')
    KAFKA_TOPIC = os.getenv('KAFKA_TOPIC', 'imdb_topic')

    # S3 Configurations
    S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME', 'your-s3-bucket')

    # IMDB Dataset
    IMDB_DATASET_PATH = os.getenv('IMDB_DATASET_PATH', './data/imdb_1000.csv')

    # Subnets for MSK
    SUBNETS = os.getenv('SUBNETS', ['subnet-xxxxxxxx', 'subnet-xxxxxxxx']).split(',')

