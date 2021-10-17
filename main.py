import requests
from datetime import datetime

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
#
# print(response)
# print(response.status_code)
#
# #goes into more detail about error encountered
# response.raise_for_status()
#
# data = response.json()
# print(data)
# print(data["message"])
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["longitude"]
#
# iss_position = (longitude, latitude)

#------------ API parameters

paramenters = {
    "lat":43.653225,
    "lng":-79.383186,
    "formatted":0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=paramenters)
response.raise_for_status()
data=response.json()
print(data)
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)


time_now = datetime.utcnow()
print(time_now.hour)