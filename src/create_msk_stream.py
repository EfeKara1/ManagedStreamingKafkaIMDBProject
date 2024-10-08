import boto3
from botocore.exceptions import ClientError
from config import Config

def create_s3_bucket():
    s3_client = boto3.client('s3')
    try:
        s3_client.create_bucket(
            Bucket=Config.S3_BUCKET_NAME,
            CreateBucketConfiguration={
                'LocationConstraint': Config.AWS_REGION
            }
        )
        print(f"Bucket {Config.S3_BUCKET_NAME} created.")
    except ClientError as e:
        print(f"Error creating S3 bucket: {e}")

def create_msk_cluster():
    kafka_client = boto3.client('kafka', region_name=Config.AWS_REGION)
    try:
        response = kafka_client.create_cluster(
            ClusterName=Config.MSK_CLUSTER_NAME,
            KafkaVersion='2.8.0',  # Specify the Kafka version
            NumberOfBrokerNodes=2,
            BrokerNodeGroupInfo={
                'InstanceType': 'kafka.m5.large',
                'ClientSubnets': Config.SUBNETS,  # List of subnet IDs
                'EBSVolumeSize': 100
            },
            EnhancedMonitoring='PER_BROKER',
            OpenMonitoring={
                'Prometheus': {
                    'JmxExporter': {
                        'EnabledInBroker': True
                    },
                    'NodeExporter': {
                        'EnabledInBroker': True
                    }
                }
            }
        )
        print(f"MSK Cluster '{Config.MSK_CLUSTER_NAME}' created.")
    except ClientError as e:
        print(f"Error creating MSK cluster: {e}")

if __name__ == "__main__":
    create_s3_bucket()
    create_msk_cluster()

