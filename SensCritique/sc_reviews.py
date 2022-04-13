import time
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

def getcommentaire(liste_titre, liste_comm, driver):
    titre = driver.find_element(By.CLASS_NAME, 'rvi-cover-title').text
    commentaire = driver.find_element(By.CLASS_NAME, 'rvi-review-content').text
    liste_titre.append(titre)
    liste_comm.append(commentaire)

def get_review_link(url):
    soup = BeautifulSoup(requests.get(url).text, 'lxml')

    time.sleep(0.8)

    list_reviews = []

    reviews = soup.find('section', {'class': 'd-grid-main'}).find_all('article')
    for review in reviews:
        list_reviews.append(review.find('a', {'class': 'ere-review-anchor'}).get('href'))
    return list_reviews
