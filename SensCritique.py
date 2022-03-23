
from tokenize import Ignore
from selenium import webdriver
import pandas as pd
import selenium
import time

driver = webdriver.Firefox()

Liste_note = []
liste_film =[]
Liste_film_traite = []
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

time.sleep(2)

liste_film.append(driver.find_elements_by_class_name('elco-title'))
for element in range(110):
    Liste_film_traite.append(liste_film[0][element].text)

print(Liste_film_traite)