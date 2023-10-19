import requests
from twilio.rest import Client
from credentials import account_sid, auth_token, phone, spicy_senorita
import os

#Environment Variables
#Useful way to hide important info, alternative to a .gitignore file
#$ env
#$ export API_KEY=abcdefg
#
#Use os library to access environment variables
# api_key = os.environ.get("OWM_API_KEY")
#
#To call from pythonanywhere
#$ export API_KEY=abcdefg; python3 main.py



OPW_endpoint = "https://api.openweathermap.org/data/3.0/onecall"


sf_lat = 37.774929
sf_lng = -122.419418
api_key = "a0663b2e844c70ce748011e0f9560f3a"


parameters = {
    "lat" : sf_lat,
    "lon" : sf_lng,
    "exclude" : "current,minutely,daily",
    "appid" : api_key,
    }


data = requests.get(url=OPW_endpoint, params=parameters)
data.raise_for_status()
weather_data = data.json()
todays_hourly_forecast = weather_data["hourly"][:12]
will_rain = False
for hour_data in todays_hourly_forecast:
    conditions = hour_data["weather"][0]["id"]
    if conditions < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today.  Remember to bring an ☔️.",
        from_='+18553360722',
        to=phone
        )
    print(message.status)
else:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Good morning spicy señorita! 🌶️💃🏻😘",
        from_='+18553360722',
        to=spicy_senorita
        )

    print(message.status)