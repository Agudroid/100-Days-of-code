import datetime

import requests

NUTRIONIX_API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": "",
    "x-app-key": ""
}

query = input("What exercise did you do?")

body = {
    "query": query
}

response = requests.post(url=NUTRIONIX_API_ENDPOINT, headers=headers, json=body)
print(response.text)

today = datetime.datetime.now()
today_date = today.strftime("%d/%m/%Y")
today_hour = today.strftime("%H:%M:%S")
print(today_hour)

for exercise in response.json()['exercises']:
    new_row = {
        "workout": {
            "date": today_date,
            "time": today_hour,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }
    response = requests.post(url="https://api.sheety.co/api_key/myWorkouts/workouts"
                             , json=new_row)
    print(response.text)


