import requests
from datetime import datetime
import smtplib

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
print(sunrise)
print(sunset)
time_now = datetime.now()

is_iss_near = (MY_LAT - 5 <= iss_latitude or iss_latitude <= MY_LAT + 5 and
               MY_LONG - 5 <= iss_longitude or iss_longitude <= MY_LONG + 5)

is_currently_dark = sunset <= time_now.hour or sunrise >= time_now.hour

if is_currently_dark and is_iss_near:
    email_account = "aguchu2000m@gmail.com"
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.login(user=email_account, password="placeholder")
    connection.sendmail(from_addr=email_account,
                        to_addrs="agudonio@outlook.com",
                        msg="Subject:Look Up\n\n"
                            "The ISS is over your head!!")
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



