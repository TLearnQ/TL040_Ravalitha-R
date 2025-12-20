
import requests

api_url = "https://httpbin.org/path"

payload = {"mode":"test"}

response=requests.patch(api_url,payload)
print("json file")
response.json()