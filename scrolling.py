# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
# driver=webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
# driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
# driver.maximize_window()
#
# #1. scroll down page by pixel
# #driver.execute_script("window.scrollBy(0,1000)","")                     # 1st approch
#
# # 2. scroll down page till the element is visible                        # 2nd approch
# # togo_flag=driver.find_element(By.XPATH,"//*[@id='content']/div[2]/div[2]/table[2]/tbody/tr[84]/td[1]/img")
# # driver.execute_script("arguments[0].scrollIntoView();",togo_flag)
#
#
# # 3. scroll down page till end                                           # 3rd approch
# driver.execute_script("window.scroll(0,document.body.scrollHeight)")

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.find_element(By.XPATH,"//input[@name='email' and @id='email']").send_keys("suzuki406")
driver.find_element_by_xpath("//input[@name='pass' and @id='pass']").send_keys("welcome@ad1")
