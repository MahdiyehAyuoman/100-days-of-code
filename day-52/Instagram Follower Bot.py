from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import ElementClickInterceptedException



SIMILAR_ACCOUNT = '-----'
USERNAME = '-----'
PASSWORD = '---'

class InstaFollower():
    def __init__(self):
        # self.URL = 'https://www.instagram.com/'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
       

    def login(self):
        URL = 'https://www.instagram.com/'
        self.driver.get(URL)

        time.sleep(10)
        self.username_input = self.driver.find_element(By.NAME, value='username')
        self.username_input.send_keys(USERNAME)
        self.password_input = self.driver.find_element(By.NAME, 'password')
        self.password_input.send_keys(PASSWORD)

        time.sleep(10)
        self.login_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/button/div')
        self.login_button.click()

        time.sleep(30)
        self.save_info  = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        if self.save_info :
            self.save_info .click()


    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")
        time.sleep(20)
        modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
        for i in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(10)

    def follow(self):
            all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')

            for button in all_buttons:
                try:
                    button.click()
                    time.sleep(1.1)
                except ElementClickInterceptedException:
                    cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                    cancel_button.click()



bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()