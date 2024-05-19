import requests
from twilio.rest import Client

parameters = {
    "lat": 40.305012,
    "lon": 3.732700,
    "appid": ""
}

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)



def is_raining(weather_list):
    for i in range(0, 4):
        weather = weather_list[i]['weather'][0]['id']
        if weather < 700:
            return True
    return False


response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
hourly_weather_list = response.json()['list']

text = "Va a llover" if is_raining(hourly_weather_list) else None
if text is not None:
    message = client.messages.create(
        from_='',
        body='Va a llover',
        to='+'
    )


