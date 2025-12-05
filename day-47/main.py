import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.header import Header


URL = "https://appbrewery.github.io/instant_pot/"

# Write your code below this line 👇
response = requests.get(URL)
movie_website = response.text
# print(movie_website)

soup = BeautifulSoup(movie_website, 'html.parser')
## Get the price
price_whole = soup.find(name='span', class_="a-price-whole")
price_decimal = soup.find(name='span', class_="a-price-fraction")
procuct_now_price = float(price_whole.get_text() + price_decimal.get_text())
# print(type(price))

procuct_title = soup.find(name='span', id="productTitle").get_text()
# print(procuct_title)

## Sending Email
if procuct_now_price < 100:
    my_gmail = 'mahdiyehayuoman@gmail.com'
    gmail_password = 'write your pass'
    uni_mail = 'm.ayuoman@iasbs.ac.ir'
    
    email_body = f"{procuct_title} is now ${procuct_now_price}\n\n{URL}"

    msg = MIMEText(email_body, 'plain', 'utf-8')

    msg['Subject'] = Header("Amazon Price Alert! ;)", 'utf-8')
    msg['From'] = my_gmail
    msg['To'] = uni_mail

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=gmail_password)
        
        connection.sendmail(from_addr=my_gmail, 
                            to_addrs=[uni_mail], 
                            msg=msg.as_string())
        
        connection.close()
        


