from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="C:\driver\chromedriver")
driver.get("http://newtours.demoaut.com/")
print(driver.title)
time.sleep(10)


driver.get("https://www.facebook.com/")
print(driver.title)
time.sleep(10)

driver.back()
print(driver.title)
time.sleep(10)

driver.forward()
print(driver.title)
time.sleep(10)

driver.close()