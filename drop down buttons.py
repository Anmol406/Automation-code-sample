# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
#
#
# driver=webdriver.Chrome(executable_path="C:\driver\chromedriver")
# driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
# #drop=Select (driver.find_element_by_id("RESULT_RadioButton-9"))
# element= driver.find_element_by_id("RESULT_RadioButton-9")
# drop= Select(element)
#
#
# #select by visible text
# #drop.select_by_visible_text("Morning")
#
# #select by index
# #drop.select_by_index("2")    #afternoon
#
# #select by value
# drop.select_by_value("Radio-2")



# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select


# driver=webdriver.Chrome(executable_path="C:\driver\chromedriver")
# driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
#
# driver.find_element(By.ID,'RESULT_TextField-1').send_keys("Anmol")
# driver.find_element(By.ID,'RESULT_TextField-2').send_keys("Dhiman")
# driver.find_element(By.ID,'RESULT_TextField-3').send_keys("+91-7508029316")
# driver.find_element_by_id("RESULT_TextField-4").send_keys("India")
# driver.find_element_by_xpath("//*[@id='q26']/table/tbody/tr[1]/td/label").click()
# driver.find_element_by_xpath("//*[@id='q15']/table/tbody/tr[1]/td/label").click()
# driver.find_element_by_xpath("//*[@id='q15']/table/tbody/tr[2]/td/label").click()
# driver.find_element_by_xpath("//*[@id='q15']/table/tbody/tr[5]/td/label").click()
# driver.find_element_by_xpath("//*[@id='q15']/table/tbody/tr[7]/td/label").click()
#
# element= driver.find_element_by_id("RESULT_RadioButton-9")
# drop= Select(element)
#
# drop.select_by_index("2")


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver=webdriver.Chrome(executable_path="C:\driver\chromedriver")
driver.get("https://www.facebook.com/")
driver.find_element_by_id("email").send_keys("suzuki406")
driver.find_element_by_id("pass").send_keys("welcome@ad1")
driver.find_element_by_id("u_0_b").click()
time.sleep(20)
person_name=driver.find_element_by_name("q")
time.sleep(30)
person_name.send_keys(" Navjot singh ")
#time.sleep(5)
#driver.find_element_by_class_name("_585_").click()
#driver.find_element_by_xpath("//*[@id='js_t']/form/button/i").click()
driver.find_element_by_xpath("//button[@type='submit' and @data-testid='facebar_search_button']").click()
#driver.find_element_by_css_selector("input[value=_585_]")
time.sleep(20)
driver.find_element_by_xpath("//*[@id='u_0_c']/a").click()
time.sleep(10)
driver.find_element_by_name("q").send_keys(" Navjot singh ")
driver.find_element_by_class_name("_585_").click()
driver.implicitly_wait(20)
element=driver.find_element_by_id("userNavigationLabel").click()
time.sleep(30)
driver.find_element_by_xpath("//span[contains(text(),'Log Out')]").click()

#driver.find_element_by_xpath("//*[@id='u_22_3']").click()




# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# import time
#
# driver=webdriver.Chrome(executable_path="C:\driver\chromedriver")
# driver.get("https://www.facebook.com/")
# driver.find_element_by_xpath("//input[@data-type='text' and @name='firstname']").send_keys("kagaj")
# #driver.find_element_by_xpath("//input[@type='text' and @id='u_0_m']").send_keys("kagaj")
# # driver.find_element_by_id("u_0_m").send_keys("kagaj")
# driver.find_element_by_id("u_0_o").send_keys("kashti")
# driver.find_element_by_id("u_0_r").send_keys("7986416565")
# driver.find_element_by_id("password_step_input").send_keys("kagajkashti7986416565")
#
# day=driver.find_element_by_id("day")
# drop= Select(day)
# drop.select_by_value(value="31")
# month=driver.find_element_by_id("month")
# drop= Select(month)
# drop.select_by_value(value="12")
# year=driver.find_element_by_id("year")
# drop= Select(year)
# drop.select_by_value(value="1992")
# #driver.find_element_by_xpath("//input[@id='u_0_7']").click()
# driver.find_element_by_xpath("//input[@type='radio' and @value='2']").click()
#driver.find_element_by_xpath("//button[@type='submit' and @name='websubmit']").click()