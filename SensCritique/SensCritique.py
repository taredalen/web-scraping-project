
from tokenize import Ignore
from webbrowser import get
from selenium import webdriver
import pandas as pd
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json


from SCget_review import getCommentaire
from SCget_review import merge_comms
from test import get_review_link

driver = webdriver.Firefox()

Liste_note = []
liste_film = []
Liste_film_traite = []
Liste_film_to_search = []

driver.get("https://www.senscritique.com/")
time.sleep(5)
driver.find_element(By.CLASS_NAME,"fc-button-label").click()
time.sleep(5)
driver.find_element(By.CLASS_NAME,'header-navigation-main-item').click()
time.sleep(5)
driver.find_element(By.LINK_TEXT,'TOPS').click()
time.sleep(5)
driver.find_element(By.CLASS_NAME,'epca-title').click()
time.sleep(5)

#Todo: les pubs surprises à prévoir/anticiper

liste_film.append(driver.find_elements(By.CLASS_NAME,'elco-title'))
for element in range(100):
    Liste_film_traite.append(liste_film[0][element].text)
#print(liste_film)

for film in range (len(Liste_film_traite)):
    Liste_film_traite[film] = Liste_film_traite[film].replace("("," ")
    Liste_film_traite[film] = Liste_film_traite[film].replace(")","")
    Liste_film_traite[film] = Liste_film_traite[film].split("  ")


Liste_commentaire = []
Liste_commentaire_titre = []
Liste_result = []
film_data2 = []
Liste_result2 = []

for titre in range(len(Liste_film_traite)):
    recherche = driver.find_element(By.CLASS_NAME,'_25jdusMm9PFEdy9TPVD0IK')
    recherche.send_keys(Liste_film_traite[titre][0])
    time.sleep(2)
    Explorer = driver.find_element(By.CLASS_NAME,'_3mHi2AhyGxzjT4yEFxyS1g')
    time.sleep(2)
    Explorer.click()
    time.sleep(2)
    genre = driver.find_elements(By.CLASS_NAME,'lahe-breadcrumb-anchor')[2].text
    time.sleep(2)
    Score = driver.find_element(By.CLASS_NAME,'pvi-scrating-value').text
    critiques = driver.find_elements(By.CLASS_NAME,'d-menu-item')[2].click()
    current_link = driver.current_url
    review_link = get_review_link(current_link)
    for critique in review_link:
        link = driver.find_element(By.XPATH,'//a[@href="'+critique+'"]').click()
        getCommentaire(Liste_commentaire_titre,Liste_commentaire,driver)
        driver.back()
        time.sleep(2)
        
    
    time.sleep(2)
    for nb_comm in range(len(Liste_commentaire)):
        dictionaire = {
            "titre_commentaire": Liste_commentaire_titre[nb_comm],
            "commentaire": Liste_commentaire[nb_comm]
            }
        Liste_result.append(dictionaire)
    film_data = {
        "titre_du_film": Liste_film_traite[titre][0],
        "annnee": Liste_film_traite[titre][1],
        "genre": genre,
        "score": Score,
        "result": [Liste_result]
        }
    film_data2.append(film_data)
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
    Liste_result = []
    Liste_commentaire_titre = []
    Liste_commentaire = []
    time.sleep(2)
    
with open('data_Senscritique.json','w') as outfile:
   json.dump(film_data2, outfile, indent = 1)

driver.close()