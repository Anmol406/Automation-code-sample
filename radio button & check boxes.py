from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\driver\chromedriver")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
#working with radio button
status=driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print(status)
driver.find_element_by_xpath("//*[@id='q26']/table/tbody/tr[1]/td/label").click()    #male
#driver.find_element_by_xpath("//*[@id='q26']/table/tbody/tr[2]/td/label").click()  #female
status=driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print(status)
driver.find_element_by_xpath("//*[@id='q15']/table/tbody/tr[1]/td/label").click()
driver.find_element_by_xpath("//*[@id='q15']/table/tbody/tr[2]/td/label").click()
driver.find_element_by_xpath("//*[@id='q15']/table/tbody/tr[5]/td/label").click()
driver.find_element_by_xpath("//*[@id='q15']/table/tbody/tr[7]/td/label").click()