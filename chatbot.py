from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch
import requests

app = Flask(__name__)
es =  Elasticsearch("http://rishipatel:rishipatel@localhost:9200")


def search_api(query):
    body = {
        "query": {
            "match": {
                "description": query
            }
        }
    }
    res = es.search(index="api_index", body=body)
    return res['hits']['hits']


@app.route('/query', methods=['POST'])
def query():
    user_query = request.json.get('query')
    results = search_api(user_query)

    if not results:
        return jsonify({"message": "No matching API found"}), 404

    api_details = results[0]['_source']
    print('api details ', api_details)

    # Check if the required parameters are provided in the request
    required_params = api_details.get('required_params', [])
    missing_params = [param for param in required_params if param not in request.json]

    if missing_params:
        return jsonify({"message": f"Missing required parameters: {', '.join(missing_params)}",
                        "required_params": required_params})

    # Make the API call if all required parameters are present
    response = make_api_call(api_details, request.json)

    return jsonify(response)


def make_api_call(api_details, user_params):
    url = api_details['url']
    method = api_details['method']
    params = {key: user_params[key] for key in api_details.get('required_params', [])}

    if method == 'GET':
        response = requests.get(url, params=params)
    elif method == 'POST':
        response = requests.post(url, json=params)

    return response.json()


if __name__ == '__main__':
    app.run(debug=True)
