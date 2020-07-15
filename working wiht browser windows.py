from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver=webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Register.html")
time.sleep(5)
driver.find_element(By.PARTIAL_LINK_TEXT,"SwitchTo").click()
time.sleep(5)
driver.find_element_by_partial_link_text("Windows").click()
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='Tabbed']/a/button").click()
print(driver.current_window_handle)                                   #parent window handle
handles=driver.window_handles                                         #returns all the handle values of opened browser windows
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    #if driver.title=="Frames & windows":                            #closes the parent window
    if driver.title=="sakinalium.in":                                #this will close the opened window's working
        driver.close()

driver.quit()