import datetime
import requests

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

USERNAME = "agudo"
# user_params = {
#     "token": TOKEN,
#     "username": "agudo",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)
#
# GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
#
# graph_config = {
#     "id": "graph1",
#     "name": "Programing habit",
#     "unit": "min",
#     "type": "int",
#     "color": "sora"
# }
#
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
#
# response = requests.post(url=GRAPH_ENDPOINT, headers=headers, json=graph_config)
# print(response.text)

pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1"

headers = {
    "X-USER-TOKEN": TOKEN
}

today = datetime.datetime.now().strftime('%Y%m%d')
quantity = str(input("How many min do you program today?"))

pixel_config = {
    "date": today,
    "quantity": quantity
}

response = requests.post(url=pixel_endpoint, headers=headers, json=pixel_config)
print(response.text)

