import requests
from datetime import datetime
import smtplib
from credentials import my_email, password
import time

MY_EMAIL = my_email
MY_PASSWORD = password
MY_LAT = 37.824100
MY_LNG = -122.373690

response = requests.get(url = "http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

iss_position = (iss_latitude, iss_longitude)
# print(iss_position)

def is_overhead(MY_LAT, MY_LNG, iss_latitude, iss_longitude):
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5:
        return True


parameters = {
    "lat" : MY_LAT,
    "lng" : MY_LNG,
    "formatted" : 0
}
response = requests.get(url = "https://api.sunrise-sunset.org/json", params = parameters)
response.raise_for_status()

data = response.json()

def PTZ_adjustment(time):
    if time < 13:
        return time - 7 * -1
    else:
        return time - 7
    

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
# print(sunrise)
# print(sunset)
ptz_sunrise = PTZ_adjustment(sunrise)
ptz_sunset = PTZ_adjustment(sunset)
# print(ptz_sunrise)
# print(ptz_sunset)

time_now = datetime.now().hour
# print(time_now)

def is_dark(ptz_sunrise, ptz_sunset, time_now):
    if time_now.hour < ptz_sunrise and time_now.hour < ptz_sunset:
        return True

count = 0
while True:
    time.sleep(60)
    count += 1
    print(count)
    if is_overhead(MY_LAT, MY_LNG, iss_latitude, iss_longitude) and is_dark(ptz_sunrise, ptz_sunset, time_now):
        with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
                connection.starttls()
                connection.login(user = MY_EMAIL, password = MY_PASSWORD)
                connection.sendmail(
                    from_addr = MY_EMAIL, 
                    to_addrs = "singzonseeds@yahoo.com",
                    msg = f"Subject:Go see ISS!\n\nYour API is telling you the International Space Station is overhead.  Remember, 3rd brightest object in the sky second to the Sun and the Moon.  You have roughly 90 minutes of viewing time - hurry!"
                    )