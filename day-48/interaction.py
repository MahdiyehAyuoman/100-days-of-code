from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

wikipedia_ulr = 'https://en.wikipedia.org/wiki/Main_Page'


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver = webdriver.Chrome(options=chrome_options)
driver.get(wikipedia_ulr)
article_numbers = driver.find_element(By.XPATH, '//*[@id="articlecount"]/ul/li[2]/a[1]')
print(article_numbers.text)


driver.close()