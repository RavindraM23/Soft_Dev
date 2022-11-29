import json, requests

#response = requests.get("https://api.stuyspec.com/")
response = requests.get("https://api.stuyspec.com/articles/what-the-duck")
response = response.json()

print(response["preview"])
