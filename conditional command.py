# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# import time
# driver=webdriver.Chrome(executable_path="C:\driver\chromedriver")
#
# driver.get("http://newtours.demoaut.com/")
# username_ele=driver.find_element_by_name("userName")
#
# print(username_ele.is_displayed())
# print(username_ele.is_enabled())
#
# password_ele=driver.find_element_by_name("password")
#
# print(password_ele.is_displayed())
# print(password_ele.is_enabled())
#
# username_ele.send_keys("mercury")
# password_ele.send_keys("mercury")
#
# driver.find_element_by_name("login").click()
#
# roundtrip=driver.find_element_by_css_selector("input[value=roundtrip]")
# print("status of roundtrip button =", roundtrip.is_selected())
#
# oneway=driver.find_element_by_css_selector("input[value=oneway]")
# print("status of oneway button =", oneway.is_selected())



from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\driver\chromedriver")
import time

driver.get("https://www.facebook.com/")
driver.implicitly_wait(50)

email_ele=driver.find_element_by_name("email")

print(email_ele.is_enabled())
print(email_ele.is_displayed())
email_ele.send_keys("suzuki406")

password_ele=driver.find_element_by_name("pass")

print(password_ele.is_enabled())
print(password_ele.is_displayed())
password_ele.send_keys("welcome@ad1")

driver.find_element_by_xpath("//*[@id='u_0_b']").click()
driver.find_element_by_name("q").send_keys("jatinder pal singh")
driver.implicitly_wait(10)
driver.find_element_by_class_name("_585_").click()

