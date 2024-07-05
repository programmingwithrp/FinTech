from elasticsearch import Elasticsearch, helpers

# Connect to Elasticsearch
es = Elasticsearch("http://rishipatel:rishipatel@localhost:9200")

# Define some sample API data with required parameters
api_data = [
    {
        "_index": "api_index",
        "_id": "1",
        "_source": {
            "name": "payment_api",
            "description": "Fetches payment details",
            "url": "http://localhost:5001/payment",
            "method": "POST",
            "required_params": ["phone_num", "otp", "password"]
        }
    },
    {
        "_index": "api_index",
        "_id": "2",
        "_source": {
            "name": "dummy_weather_api",
            "description": "Provides dummy weather information",
            "url": "http://localhost:5001/dummy_weather",
            "method": "GET",
            "required_params": ["city"]
        }
    }
]

# Index the data
helpers.bulk(es, api_data)
