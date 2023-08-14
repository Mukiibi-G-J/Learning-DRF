import requests

# endpoint = "https://httpbin.org/status/200"
endpoint = "http://localhost:8000/api/products/1/update"
# endpoint = "https://httpbin.org/anything"
data = {"title": "this is the new title", "price": 122.9}

get_response = requests.put(endpoint, json=data)


print(get_response.json())
