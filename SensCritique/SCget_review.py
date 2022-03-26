from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


driver = webdriver.Firefox()
driver.get("https://www.senscritique.com/")

Liste_commentaire = []
Liste_commentaire_titre = []

def getCommentaire():
    Liste_commentaire_titre.append(driver.find_elements(By.CLASS_NAME,'ere-review-heading').text)
    Liste_commentaire.append(driver.find_elements(By.CLASS_NAME,'ere-review-excerpt').text)


def merge_comms(liste_comm,liste_titre):
    Frame_commentaire = pd.DataFrame({"titre":liste_titre,"commentaire":liste_comm})
    Frame_commentaire.to_csv('SensCritique.csv',sep = ";")
    return Frame_commentaire

def recherche(titre):
    recherche = driver.find_element(By.CLASS_NAME,'_1ubz4flJX9nhcvdMnRV6CA')
    recherche.send_keys(titre)