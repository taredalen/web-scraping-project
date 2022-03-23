from csv import list_dialects
from tokenize import Ignore
from selenium import webdriver
import pandas as pd
import selenium
import time

driver = webdriver.Firefox()

Liste_note = []
liste_film =[]
driver.get("https://www.senscritique.com/")
time.sleep(5)
#driver.find_element(by= By.CLASS_NAME, value="fc-button-label").click()
driver.find_element_by_class_name("fc-button-label").click()
time.sleep(5)
driver.find_element_by_class_name('header-navigation-main-item').click()
time.sleep(5)
driver.find_element_by_link_text('TOPS').click()
time.sleep(5)
driver.find_element_by_class_name('epca-title').click()
time.sleep(5)

#if driver.find_element_by_class_name('sas-btn-skip sas-enable')==True:
#    driver.find_element_by_class_name('sas-btn-skip sas-enable').click()

time.sleep(2)
driver.find_elements_by_class_name('elco-anchors')
print(driver.find_elements_by_class_name('d-heading2 elco-title'))

#Films = pd.DataFrame({"Nom_Film":liste_film,"Note":Liste_note})