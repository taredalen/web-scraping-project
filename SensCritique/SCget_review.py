from datetime import time
from selenium import webdriver

from selenium.webdriver.common.by import By
import pandas as pd
from bs4 import BeautifulSoup
import requests


def getCommentaire(Liste_titre, liste_comm, driver):
    titre2 = driver.find_element(By.CLASS_NAME, 'rvi-cover-title').text
    commentaire = driver.find_element(By.CLASS_NAME, 'rvi-review-content').text
    Liste_titre.append(titre2)
    liste_comm.append(commentaire)



def merge_comms(liste_titre,liste_comm):
    Frame_commentaire = pd.DataFrame({"titre_comm":liste_titre,"commentaire":liste_comm})
    Frame_commentaire.to_csv('SensCritique.csv',sep = ";")
    return Frame_commentaire

def get_Critique(driver):
    driver = webdriver.firefox()
    driver.get()