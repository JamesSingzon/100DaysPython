from credentials import app_id, api_key, sheety_url, user, passcode
import requests
from datetime import datetime


APP_ID = app_id
API_KEY = api_key
GENDER = "male"
WEIGHT = 90.72
HEIGHT = 182.88
AGE = 32

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise = input("Tell me which exercises you did: ")
# exercise = "ran 3 miles"


nutritionix_config = {
    "query":exercise,
    "gender":GENDER,
    "weight_kg":WEIGHT,
    "height_cm":HEIGHT,
    "age":AGE
}

headers = {
    "x-app-id":APP_ID,
    "x-app-key":API_KEY,
    "x-remote-user-id": "0"
}


response = requests.post(url=nutritionix_endpoint,json=nutritionix_config,headers=headers)
# print(response.text)
result = response.json()["exercises"][0]
exercise_type = result["user_input"].title()
exercise_duration = int(result["duration_min"])
exercise_calories = int(result["nf_calories"])

sheety_endpoint = sheety_url

today = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")

sheety_json = {
    "workout": {
        "date":today,
        "time":time,
        "exercise":exercise_type,
        "duration":exercise_duration,
        "calories":exercise_calories
    }
}

response = requests.post(url=sheety_endpoint,json=sheety_json,auth=(user, passcode))
print(response.text)