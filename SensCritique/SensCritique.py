
from tokenize import Ignore
from webbrowser import get
from selenium import webdriver
import pandas as pd
import selenium
from selenium.webdriver.common.by import By
import time
import json


from SCget_review import getCommentaire
from SCget_review import merge_comms
from SCget_review import traitement_valeurs

driver = webdriver.Firefox()

Liste_note = []
liste_film = []
liste_film_annee = []
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


Data_imdb = pd.read_json('./IMDB/data.json')


for titre in range(3):
    Liste_commentaire = []
    Liste_commentaire_titre = []
    recherche = driver.find_element(By.CLASS_NAME,'_25jdusMm9PFEdy9TPVD0IK')
    recherche.send_keys(Liste_film_traite[titre][0])
    time.sleep(5)
    Explorer = driver.find_element(By.CLASS_NAME,'_3mHi2AhyGxzjT4yEFxyS1g')
    time.sleep(5)
    Explorer.click()
    time.sleep(2)
    getCommentaire(Liste_commentaire_titre,Liste_commentaire,driver)
    time.sleep(2)


traitement_valeurs(Liste_commentaire_titre)
traitement_valeurs(Liste_commentaire)

for annee in Liste_film_traite:
    liste_film_annee.append(annee[1])

for i in range (len(Liste_commentaire_titre)):
    dictionnary = {
        'titre' : Liste_commentaire_titre[0][i],
        'commentaire' : Liste_commentaire[0][i]
    }
    Film_data = {"title": Liste_film_traite[i], "result": dictionnary }

"""
====================================================================

MSG pour yohan
pr l'instant l'intégration dans le fichier json écrale les valeurs précédantes 
parceque je stocke les valeur directement dans le fichier json.Il faudrais que tu 
stocke les valeur dans une liste externe et que ensuite tu le met dans le fichier json
n'oublie pas de le faire dans le même format que le ficheir json de nos coéquipier

====================================================================

"""

with open('data_Senscritique.json','w') as outfile:
   json.dump(Film_data, outfile, indent = 1)

driver.close()