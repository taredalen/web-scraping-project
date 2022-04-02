import time

from selenium.webdriver.common.by import By
import pandas as pd
from bs4 import BeautifulSoup
import requests

def get_review_link(url):
    soup = BeautifulSoup(requests.get(url).text, 'lxml')

    time.sleep(0.8)

    list_reviews = []

    reviews = soup.find('section', {'class': 'd-grid-main'}).find_all('article')
    for review in reviews:
        list_reviews.append(review.find('a', {'class': 'ere-review-anchor'}).get('href'))
    return list_reviews