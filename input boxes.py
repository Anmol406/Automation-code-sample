from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\driver\chromedriver")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")


# how to find how many value boxes are there on the page
inputboxes=driver.find_elements(By.CLASS_NAME,'text_field')
print(len(inputboxes))  #6
status=driver.find_element(By.ID,'RESULT_TextField-1').is_displayed()
print(status)
status=driver.find_element(By.ID,'RESULT_TextField-1').is_enabled()
print(status)
#how to provide value into text boxes

driver.find_element(By.ID,'RESULT_TextField-1').send_keys("Anmol")
driver.find_element(By.ID,'RESULT_TextField-2').send_keys("Dhiman")
driver.find_element(By.ID,'RESULT_TextField-3').send_keys("+91-7508029316")
driver.find_element_by_id("RESULT_TextField-4").send_keys("India")
