import json, requests

#response = requests.get("https://api.stuyspec.com/")
#response = requests.get("https://api.stuyspec.com/articles/what-the-duck")
#response = response.json()

response = requests.get("https://api.sunrise-sunset.org/json")

print(response.text)
