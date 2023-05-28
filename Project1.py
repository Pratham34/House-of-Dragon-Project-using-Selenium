from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

path = "C:/selenium/chromedriver.exe"
s = Service(path)
driver = webdriver.Chrome(service = s)
driver.get("https://www.google.com/")
time.sleep(2)

box = driver.find_element(By.XPATH,'//*[@id="APjFqb"]')
box.send_keys("House of Dragon")
box.send_keys(Keys.ENTER)
time.sleep(3)

driver.find_element(By.XPATH,'//*[@id="kp-wp-tab-overview"]/div[4]/div/div/div/div/div/div[1]/div/a').click()
time.sleep(2)

driver.save_screenshot("D:/Academics/wscube web scraping using python/4. Mini Proj of House of Dragon using Selenium/dragon1.png")