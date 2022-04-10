import time
from selenium import webdriver

from selenium.webdriver.common.by import By
import pandas as pd
from bs4 import BeautifulSoup
import requests


def getcommentaire(Liste_titre, liste_comm, driver): #TODO: PEP 8
    titre2 = driver.find_element(By.CLASS_NAME, 'rvi-cover-title').text
    commentaire = driver.find_element(By.CLASS_NAME, 'rvi-review-content').text
    Liste_titre.append(titre2)
    liste_comm.append(commentaire)

def get_review_link(url):
    soup = BeautifulSoup(requests.get(url).text, 'lxml')

    time.sleep(0.8)

    list_reviews = []

    reviews = soup.find('section', {'class': 'd-grid-main'}).find_all('article')
    for review in reviews:
        list_reviews.append(review.find('a', {'class': 'ere-review-anchor'}).get('href'))
    return list_reviews
