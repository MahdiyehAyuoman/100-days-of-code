import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 35.715718 # Your latitude
MY_LONG = 51.365530 # Your longitude
first_gmail = 'mahdiyehayuoman@gmail.com'
gmail_password = 'write your password'
second_mail = 'write your email'

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

time_now = datetime.now().hour
# print(time_now.hour)


while True:
    time.sleep(60)
    #If the ISS is close to my current position
    if iss_latitude in range(MY_LAT - 5, MY_LAT + 5) and iss_longitude in range(MY_LONG - 5, MY_LONG + 5):

        # and it is currently dark
        if time_now >= sunset or time_now < sunrise:

            # Then send me an email to tell me to look up
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=first_gmail, password=gmail_password)
                connection.sendmail(from_addr=first_gmail, 
                                    to_addrs=second_mail, 
                                    msg=(f"subject:Look Up!\n\nThe ISS is above you in the sky!"))
                connection.close()
