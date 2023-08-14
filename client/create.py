import requests

data = {"title": "people", "price": 32.4}

# endpoint = "https://httpbin.org/status/200"
endpoint = "http://localhost:8000/api/products/"
# endpoint = "https://httpbin.org/anything"
get_response = requests.post(endpoint, data)

print(get_response.json())
