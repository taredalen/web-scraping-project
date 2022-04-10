import time
import warnings

import requests
from bs4 import BeautifulSoup

warnings.filterwarnings('ignore')

def get_critics_reviews(url):

    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'lxml')
    reviews = soup.find_all("a", {"class": "tracked-offsite-link"})
    filters = ["Roger Ebert", "ReelViews", "Washington Post", "rogerebert.com", "New York Times"] #contient tout les critiques que je veux scrap
    review_list = []
    for review in reviews:
        if any(filter in review.text for filter in filters): 
            time.sleep(0.8)
            req = requests.get(review.get("href"))
            paragraphe = BeautifulSoup(req.text, "lxml").find_all("p")
            text_review = " ".join([text.text for text in paragraphe])
            review_list.append({"title": review.text.strip(), "content": text_review})
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
