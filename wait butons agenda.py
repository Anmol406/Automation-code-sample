# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# driver=webdriver.Chrome(executable_path="C:\driver\chromedriver")
# import time
# driver.get("http://newtours.demoaut.com/")
# driver.implicitly_wait(40)
#
# assert "Welcome: Mercury Tours" in driver.title
# username_ele=driver.find_element_by_name("userName").send_keys("mercury")
# password_ele=driver.find_element_by_name("password").send_keys("mercury")
#
# driver.find_element_by_name("login").click()



# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# driver=webdriver.Chrome(executable_path="C:\driver\chromedriver")
# driver.get("https://www.youtube.com/")
#
#
# driver.find_element_by_name("search_query").send_keys("Goblins from Mars - Cold Blooded Love (ft. Krista Marina")
# driver.find_element_by_id("search-icon-legacy").click()


                                         #EXPLICIT WAIT

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# driver=webdriver.Chrome(executable_path="C:\driver\chromedriver")
#
# driver.maximize_window()
# driver.get("https://www.goibibo.com/")
#
# driver.find_element_by_id("multiCity").click()
# driver.find_element_by_id("gosuggest_inputSrc").send_keys("chennai (MAA)")
# driver.find_element_by_id("gosuggest_inputDest").send_keys("chandigarh (IXC)")
# driver.find_element_by_id("footer").send_keys("27 july 2020")
# #driver.find_element_by_id("")


# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# driver=webdriver.Chrome(executable_path="C:\driver\chromedriver")
# driver.implicitly_wait(10)
#
# driver.get("https://www.expedia.co.in/United-States-Of-America.d201.Holidays-City-Breaks")
# driver.find_element_by_id("tab-flight").click()
# driver.implicitly_wait(20)
# driver.find_element_by_id("F-origin").send_keys("new york")
# time.sleep(5)
# driver.find_element_by_id("F-destination").clear()
# driver.find_element_by_id("F-destination").send_keys("las vegas")
# time.sleep(5)
# driver.find_element_by_id("F-fromDate").send_keys("12/10/2020")
# #driver.implicitly_wait(30)
# driver.find_element_by_id("F-toDate").clear()
# driver.find_element_by_id("F-toDate").send_keys("1/10/2020")
# #driver.implicitly_wait(30)
# driver.find_element_by_id("F-searchButtonExt1").click()
# #driver.find_element_by_xpath("//*[@id='FH-searchButtonExt1']").click()
# driver.implicitly_wait(10)
# driver.find_element_by_id("stopFilter_stops-0").click()
# driver.implicitly_wait(10)
# driver.find_element_by_id("stopFilter_stops-1").click()
# driver.implicitly_wait(10)
#
# wait=WebDriverWait(driver,20)
# #element=wait.until(EC.element_to_be_clickable(find_element_by_xpath("//*[@id='airlineRowContainer_AA']")))
# element=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='airlineRowContainer_AA']")))
# element.click()
#
# time.sleep(10)
# driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# import time
#
# driver=webdriver.Chrome(executable_path="C:\driver\chromedriver")
#
# driver.get("https://www.facebook.com/")
# driver.implicitly_wait(20)
# driver.find_element_by_id("email").send_keys("suzuki406")
# driver.find_element_by_id("pass").send_keys("welcome@ad1")
# driver.find_element_by_id("u_0_b").click()
#
# wait=WebDriverWait(driver,20)
# element=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='u_0_a']/div[1]/div[1]/div/a/span/span")))
# element.click()
#
# time.sleep(30)
#driver.close()


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver=webdriver.Chrome(executable_path="C:\driver\chromedriver")

driver.get("https://www.linkedin.com")
driver.implicitly_wait(20)
driver.find_element_by_id("session_key").send_keys("anmoldhiman271992@gmail.com")
driver.find_element_by_id("session_password").send_keys("suzuki406")
driver.find_element_by_class_name("sign-in-form__password-visibility-toggle-button").click()
#driver.implicitly_wait(20)
time.sleep(10)
driver.find_element_by_class_name("sign-in-form__submit-button").click()
wait=WebDriverWait(driver, 30)
element=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='mynetwork-nav-item']/a/span[1]")))
time.sleep(20)
element.click()
driver.find_element_by_class_name("msg-overlay-bubble-header").click()
time.sleep(20)
driver.find_element_by_id("notifications-tab-icon").click()
driver.implicitly_wait(20)
#driver.find_element_by_id("ember1411").click()
driver.find_element_by_xpath("//*[@id='ember1394']").click()
time.sleep(20)
print(driver.title)