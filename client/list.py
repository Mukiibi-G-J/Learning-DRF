import requests
from getpass import getpass

# endpoint = "https://httpbin.org/status/200"
auth_endpoint = "http://localhost:8000/api/auth/"
endpoint = "http://localhost:8000/api/products/"
# endpoint = "https://httpbin.org/anything"
# password = getpass()
username = input("What is your username?\n")
password = getpass("What is your password?\n")
auth_response = requests.post(auth_endpoint, json={
    "username": username,
    "password": password
})

if auth_response.status_code == 200:
    token = auth_response.json()["token"]
    # "Authorization": f"Token {token}"

    headers = {
        "Authorization": f"Bearer {token}"

    }
    get_response = requests.get(
        endpoint, headers=headers

    )

print(get_response.json())
print(auth_response.json())
