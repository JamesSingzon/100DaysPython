import requests
from datetime import datetime

USERNAME = "jamessingzon"
TOKEN = "cckkeidps2kkb9"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":"graph1",
    "name":"Weightroom Graph",
    "unit":"day",
    "type":"int",
    "color":"kuro"
}

headers = {
    "X-USER-TOKEN":TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now().strftime("%Y%m%d")
print(today)

pixel_config = {
    "date":"20231025",
    "quantity":"1"
}

weightroom_graph_endpoint = f"{graph_endpoint}/graph1"

# response = requests.post(url=weightroom_graph_endpoint, json=pixel_config, headers=headers)
# print(response.text)