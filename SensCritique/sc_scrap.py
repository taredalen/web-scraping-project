import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from sc_reviews import getcommentaire, get_review_link

def initiate_scrapping_sc():
    driver = webdriver.Firefox()

    liste_film = []
    liste_film_text = []#TODO : verifier et supprimer des variables non utilisées
    liste_commentaire = []
    liste_commentaire_titre = []
    liste_result = []
    film_rows = []
    driver.get("https://www.senscritique.com/films/tops/top111") #TODO : remplacer avec BS ou supprimer si deja fait de 17 à 26
    time.sleep(5)
    driver.find_element(By.CLASS_NAME, "fc-button-label").click()

    #TODO: les pubs surprises à prévoir/anticiper

    liste_film.append(driver.find_elements(By.CLASS_NAME, 'elco-title'))
    for element in range(100):
        liste_film_text.append(liste_film[0][element].text)
    
    
    for film in range(len(liste_film_text)):
        liste_film_text[film] = liste_film_text[film].replace("(", " ")
        liste_film_text[film] = liste_film_text[film].replace(")", "")
        liste_film_text[film] = liste_film_text[film].split("  ")
    

    for titre in range(len(liste_film_text[0])):
        recherche = driver.find_element(By.CLASS_NAME, '_25jdusMm9PFEdy9TPVD0IK')
        recherche.send_keys(liste_film_text[titre][0])
        time.sleep(2)
        explorer = driver.find_element(By.CLASS_NAME, '_3mHi2AhyGxzjT4yEFxyS1g')
        time.sleep(2)
        explorer.click()
        time.sleep(2)
        try:
            genre = driver.find_elements(By.CLASS_NAME, 'lahe-breadcrumb-anchor')[2].text
        except IndexError:
            genre = "Null"
        time.sleep(2)
        score = driver.find_element(By.CLASS_NAME, 'pvi-scrating-value').text #TODO voir PEP 8 pour la declaration des var
        driver.find_element(By.LINK_TEXT, 'Critiques').click()
        current_link = driver.current_url
        review_link = get_review_link(current_link)
        for critique in review_link:
            driver.find_element(By.XPATH, '//a[@href="' + critique + '"]').click()
            getcommentaire(liste_commentaire_titre, liste_commentaire, driver)
            driver.back()
            time.sleep(2)

        time.sleep(2)
        for nb_comm in range(len(liste_commentaire)):
            dictionaire = {
                "titre_commentaire": liste_commentaire_titre[nb_comm],
                "commentaire": liste_commentaire[nb_comm]
            }
            liste_result.append(dictionaire)
        film_data = {
            "titre_du_film": liste_film_text[titre][0],
            "annnee": liste_film_text[titre][1],
            "genre": genre,
            "score": score,
            "result": [liste_result]
        }
        film_rows.append(film_data)
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        liste_result = []
        liste_commentaire_titre = []
        liste_commentaire = []
        time.sleep(2)
    driver.close()
    create_json(film_rows)


def create_json(film_rows):
    with open('../Data/data_sc.json', 'w') as outfile:
        json.dump(film_rows, outfile, indent=1)

initiate_scrapping_sc()

