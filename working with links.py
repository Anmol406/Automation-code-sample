# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select                                  #for drop down
# from selenium.webdriver.support.ui import WebDriverWait
# import time
# driver=webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
# driver.get("http://newtours.demoaut.com/")
# links=driver.find_elements(By.TAG_NAME,"a")                                     #"a" is a common tag name
# print("Number of links:",len(links))
# for link in links:
#     print(link.text)
#
# #driver.find_element(By.LINK_TEXT,"REGISTER").click()
# driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/a").click()
# driver.find_element(By.LINK_TEXT,"SUPPORT").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"REG").click()



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select                                  #for drop down
from selenium.webdriver.support.ui import WebDriverWait
import time


driver=webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
driver.get("https://www.amazon.in/")
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("asus zenfone 6z")
driver.find_element(By.XPATH,"//input[@type='submit' and @class='nav-input']").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"ASUS ZenBook Duo UX481FL-BM5811T Intel Core i5 10th Gen").click()
#driver.find_element_by_xpath("//*[@id='search']/div[1]/div[2]/div/span[3]/div[2]/div[1]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span").click()