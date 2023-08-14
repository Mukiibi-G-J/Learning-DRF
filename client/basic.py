import requests

# endpoint = "https://httpbin.org/status/200"
endpoint = "http://localhost:8000/api/"
# endpoint = "https://httpbin.org/anything"

# HTTP request
get_response = requests.post(
    endpoint,
    json={"content": "kali book"},
)

# return text /string /html Content-Type': 'text/html
# print(get_response.text)
print(get_response.headers)
# returns json
print(get_response.json())


# returns python dictionary


# {
#     "args": {"abc": "123"},
#     "data": "",
#     "files": {},
#     "form": {"name": "person"},
#     "headers": {
#         "Accept": "*/*",
#         "Accept-Encoding": "gzip, deflate",
#         "Content-Length": "11",
#         "Content-Type": "application/x-www-form-urlencoded",
#         "Host": "httpbin.org",
#         "User-Agent": "python-requests/2.25.1",
#         "X-Amzn-Trace-Id": "Root=1-62d6e64d-05477b653f6f4cd92b1b909c",
#     },
#     "json": null,
#     "method": "GET",
#     "origin": "154.225.153.101",
#     "url": "https://httpbin.org/anything?abc=123",
# }

# {
#     "args": {"abc": "123"},
#     "data": "",
#     "files": {},
#     "form": {"name": "person"},
#     "headers": {
#         "Accept": "*/*",
#         "Accept-Encoding": "gzip, deflate",
#         "Content-Length": "11",
#         "Content-Type": "application/x-www-form-urlencoded",
#         "Host": "httpbin.org",
#         "User-Agent": "python-requests/2.25.1",
#         "X-Amzn-Trace-Id": "Root=1-62d6e6f2-3ae424630a08cf1513c7e9d2",
#     },
#     "json": None,
#     "method": "GET",
#     "origin": "154.225.153.101",
#     "url": "https://httpbin.org/anything?abc=123",
# }
