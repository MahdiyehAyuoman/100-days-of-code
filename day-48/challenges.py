
## 4. Challenge Use Selenium to Scrape Website Data
# keeps chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.python.org/')

upcomig_event_time = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/time')
upcomig_event_name = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/a')

upcomig_event_dic = {}
for i in range(len(upcomig_event_time)):
    upcomig_event_dic[i] ={
        "time" : upcomig_event_time[i].text,
        "name" : upcomig_event_name[i].text
    }

print(upcomig_event_dic)



# Challenge: 6. How to Automate Filling Out Forms and Clicking Buttons with Selenium
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver = webdriver.Chrome(options=chrome_options)
driver.get('http://secure-retreat-92358.herokuapp.com/')

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Mahi")

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Ayoo")

email = driver.find_element(By.NAME, value="email")
email.send_keys("mahi@gamil.com")

sigh_up = driver.find_element(By.CSS_SELECTOR, value='.btn.btn-lg.btn-primary.btn-block')
sigh_up.click()

