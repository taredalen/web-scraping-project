from tokenize import Ignore
from selenium import webdriver
import selenium
import time

driver = webdriver.Firefox()
Liste_Films = []
driver.get("https://www.senscritique.com/")
time.sleep(2)
#driver.find_element(by= By.CLASS_NAME, value="fc-button-label").click()
driver.find_element_by_class_name("fc-button-label").click()
time.sleep(2)
driver.find_element_by_class_name('header-navigation-main-item').click()
time.sleep(2)
driver.find_element_by_link_text('TOPS').click()
time.sleep(2)
if  driver.find_element_by_class_name('epca-cover type-1')== True :
    driver.find_element_by_class_name('epca-cover type-1').click()
else:
    Ignore
time.sleep(2)
driver.find_element_by_class_name('epca-title').click()