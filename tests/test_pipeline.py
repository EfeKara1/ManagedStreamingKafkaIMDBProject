import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from src.producer import kafka_producer
from src.consumer import kafka_consumer
from src.config import Config

class TestKafkaPipeline(unittest.TestCase):
    @patch('src.producer.KafkaProducer')
    @patch('pandas.read_csv')
    def test_kafka_producer(self, mock_read_csv, mock_kafka_producer):
        # Mock the DataFrame returned by pandas read_csv
        mock_data = pd.DataFrame({
            'id': [1, 2],
            'name': ['Movie 1', 'Movie 2'],
            'rating': [8.5, 7.0]
        })
        mock_read_csv.return_value = mock_data
        
        producer_instance = MagicMock()
        mock_kafka_producer.return_value = producer_instance
        
        kafka_producer()
        
        self.assertEqual(producer_instance.send.call_count, 2)
    
    @patch('src.consumer.KafkaConsumer')
    @patch('src.s3_utils.upload_to_s3')
    def test_kafka_consumer(self, mock_upload_to_s3, mock_kafka_consumer):
        mock_data = {'id': 1, 'name': 'Movie 1', 'rating': 8.5}
        mock_consumer_instance = MagicMock()
        mock_consumer_instance.__iter__.return_value = [MagicMock(value=mock_data)]
        
        with patch('src.consumer.KafkaConsumer', return_value=mock_consumer_instance):
            kafka_consumer()
        
        mock_upload_to_s3.assert_called_once_with(mock_data)

if __name__ == '__main__':
    unittest.main()

