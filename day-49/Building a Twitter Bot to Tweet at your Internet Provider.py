from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = ""
TWITTER_PASSWORD = ""

class InternetSpeedTwitterBot():
    def __init__(self):

        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome()
        # wait = WebDriverWait(driver, timeout=200) 
        # self.driver.get("https://www.speedtest.net/")
        self.get_internet_speed()
        self.tweet_at_provider()

    def get_internet_speed(self):

        # wait = WebDriverWait(driver, timeout=200) 
        self.driver.get("https://www.speedtest.net/")

        time.sleep(3)
        self.go_button = self.driver.find_element(by = By.CSS_SELECTOR, value= '.start-button') ## OK
        self.go_button.click()

        time.sleep(60)
        self.download_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]')
        print(self.download_speed.text)
   
        upload_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        print(upload_speed.text)


    def tweet_at_provider(self):
        self.driver.get('https://x.com/i/flow/login')
        email_input_class = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input'
        input_email = self.driver.find_element(By.XPATH, email_input_class)
        input_email.send_keys(TWITTER_EMAIL)

        input_password = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
        input_password.send_keys(TWITTER_PASSWORD)
        time.sleep(5)
        tweet_compose = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')

        time.sleep(3)
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)

        tweet_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()


InternetSpeedTwitterBot()