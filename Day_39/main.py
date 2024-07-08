#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import requests
from pprint import pprint
import flight_search

url = "https://api.sheety.co/7b83f13ecfea7096e4d99d63761e03a7/flightDeals/prices"

response = requests.get(url)
sheet_data = response.json()["prices"]

for item in sheet_data:
    if item["iataCode"] == '':
        flight_search()

# pprint(sheet_data)