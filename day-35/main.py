import requests
import json
import smtplib


api_key = "d6d82db86f7ae73044b89d63c37240a4"
cnt = 4

## Step 1, 2, 3, 4 challange one
# response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?lat=35.695672&lon=51.381670&appid={api_key}")
response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat=35.695672&lon=51.381670&cnt={cnt}&appid={api_key}")
decoded_response = response.content.decode("UTF-8")
# print(response.status_code)
# print(decoded_response)


## Step 5, 6 challange one
data = json.loads(decoded_response)
jsonData = data["list"]

weather_id_list =[]
weather_description_list =[]
for i in range(len(jsonData)):
    weather_id = jsonData[i]['weather'][0]['id']
    weather_id_list.append(weather_id)
    weather_description = jsonData[i]['weather'][0]['description']
    weather_description_list.append(weather_description)
    # print(weather_id)
    # print(weather_description)

## challange two
# print(weather_id_list)
will_rain = False
for w in range(len(weather_id_list)):
    if weather_id_list[w] > 700:
        will_rain = True

if will_rain:
    # print("Bring an umbrella")
    # 4. Send the email for bringing an umbrella in rainy days
    my_gmail = 'mahdiyehayuoman@gmail.com'
    gmail_password = 'write your password here'
    uni_mail = 'm.ayuoman@iasbs.ac.ir'

    ## Send the quote of the day via email
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=gmail_password)
        connection.sendmail(from_addr=my_gmail, 
                            to_addrs=uni_mail, 
                            msg=(f"subject:Bring an umbrella ;)\n\nIt's going to rain. Don't forget your umbrella!"))
        connection.close()



