from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import ElementClickInterceptedException
import re
import requests
from bs4 import BeautifulSoup


ZILLOW_URL = 'https://appbrewery.github.io/Zillow-Clone/'

response = requests.get(ZILLOW_URL)
zillow_clone = response.text

soup = BeautifulSoup(zillow_clone, 'html.parser')

## Get All the house link href by class name
house_links = []
for a in soup.find_all('a', class_="property-card-link"):
    house_links.append(a['href'])

# print(house_links)

# class="PropertyCardWrapper__StyledPriceLine"

house_prices = []
for p in soup.find_all('span', class_="PropertyCardWrapper__StyledPriceLine"):
    price = p.get_text()
    price = price.replace('+/mo', '').replace('+ 1 bd','').replace('/mo','').replace('+ 1bd','')
    # print(price)
    house_prices.append(price)

# print(house_prices)

# address  ,  Clean up the address data as well. Remove any newlines, pipe symbols |, and unnecessary whitespace.
house_address = []
for s in soup.find_all('address'):
    adress = s.get_text()
    adress = adress.replace('\n', '').replace('|', '').strip()
    house_address.append(adress)

# print(house_address)


# GOOGLE_FORM_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSd5oK1Dy0TrlwWgsuI7znEQky8MxOZ7JRV31Acsfa-9sWqlJw/viewform?usp=header'

GOOGLE_FORM_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSff3PWEYXLp22iGJlaoUS-N4VvLkuHrG1cCMgSBf1mgYdBtLw/viewform?usp=publish-editor'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(GOOGLE_FORM_URL)

## Fill Adress       مشکل الان اینکه همه ی آدرسها رو تا انتها میره بعد میرع سراغ لینک و موارد دیگه این باید حل بشه در مورد محدوده ی حلقه ی for فکر کنم
for a in range(len(house_address)):
    time.sleep(5)
    path = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
    adress_input = driver.find_element(By.XPATH, path)
    adress_input.send_keys(house_address[a])

    time.sleep(5)
    price_input_path = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
    price_input = driver.find_element(By.XPATH, price_input_path)
    price_input.send_keys(house_prices[a])

    time.sleep(5)
    link_input_path = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
    link_input = driver.find_element(By.XPATH, link_input_path)
    link_input.send_keys(house_links[a])

    time.sleep(2)
    submit_path = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div'
    submit_button = driver.find_element(By.XPATH, submit_path)
    submit_button.click()

    time.sleep(5)
    another_response_path = '/html/body/div[1]/div[2]/div[1]/div/div[4]/a'
    another_response = driver.find_element(By.XPATH, another_response_path)
    another_response.click()


# for price in range(len(house_prices)):
#     time.sleep(5)
#     path = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
#     price_input = driver.find_element(By.XPATH, path)
#     price_input.send_keys(house_prices[price])

# time.sleep(5)
# for link in range(len(house_links)):
#     time.sleep(5)
#     path = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
#     link_inputt = driver.find_element(By.XPATH, path)
#     link_inputt.send_keys(house_links[link])