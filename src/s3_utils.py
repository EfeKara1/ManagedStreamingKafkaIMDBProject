import boto3
import json
from config import Config

def upload_to_s3(data):
    s3_client = boto3.client('s3')
    file_name = f"imdb_data_{data['id']}.csv"  # Adjust according to your dataset
    s3_client.put_object(Bucket=Config.S3_BUCKET_NAME, Key=file_name, Body=json.dumps(data))

