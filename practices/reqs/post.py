import requests

payload = {"key1": "value1", "key2": "value2"}

r = requests.post("http://httpbin.org/post", params=payload)
print(r.text)
