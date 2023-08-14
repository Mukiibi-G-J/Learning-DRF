import requests

# endpoint = "https://httpbin.org/status/200"
endpoint = "http://localhost:8000/api/products/4"
# endpoint = "https://httpbin.org/anything"
get_response = requests.get(
    endpoint,
)

print(get_response.json())
