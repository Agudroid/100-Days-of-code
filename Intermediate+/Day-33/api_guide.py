import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

response.raise_for_status()
data = response.json()
print(data)

parameters = {
    'lat': 40.305012,
    'lng': -3.732700,
    'formatted': 0
}

response_2 = requests.get("https://api.sunrise-sunset.org/json", parameters)
response_2.raise_for_status()
data = response_2.json()
print(data)
