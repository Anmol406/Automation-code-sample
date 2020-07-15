#IN FRAME WORK XPATH DONT WORK TO FIND THE FRAME


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# driver=webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
# driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")
# driver.switch_to.frame("packageListFrame")
# driver.find_element_by_link_text("org.openqa.selenium").click()



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")
driver.switch_to.frame("packageListFrame")                                         #FIRST FRAME
driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(5)
driver.switch_to.default_content()
driver.switch_to.frame("packageFrame")                                             #SECOND FRAME
driver.find_element_by_link_text("WebDriver").click()
time.sleep(5)
driver.switch_to.default_content()
time.sleep(5)
driver.switch_to.frame("classFrame")                                               #THIRD FRAME
driver.find_element(By.XPATH,"/html/body/div[1]/ul/li[5]/a").click()