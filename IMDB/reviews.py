from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup
import requests
import time

import warnings
warnings.filterwarnings("ignore")

def get_critics_reviews(url):
    
    header = {'User-Agent': '"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"'}
    request = requests.get(url, headers=header)
    soup = BeautifulSoup(request.text, 'lxml')
    reviews = soup.find_all("a", {"class": "tracked-offsite-link"})
    filter = ["Roger Ebert", "ReelViews", "Washington Post", "rogerebert.com", "New York Times"]
    review_list = []
    for review in reviews:
        for filt in filter:
            if filt in review.text:
                time.sleep(2)
                req = requests.get(review.get("href"))
                site = BeautifulSoup(req.text, "lxml")
                para = site.find_all("p")
                text_review = ""
                for text in para:
                    text_review += text.text
                review_list.append({review.text.strip(): text_review})

    return review_list

def get_user_reviews(url):

    soup = BeautifulSoup(requests.get(url).text, 'lxml')

    time.sleep(0.8)

    list_reviews = []

    for review in soup.find_all('div',  {'class': 'lister-item-content'}):
        dictionary = {'title': review.find('a').text,
                      'content': review.find('div', {'class': 'text show-more__control'}).text}
        list_reviews.append(dictionary)
        time.sleep(0.8)

    return list_reviews
