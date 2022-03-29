import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup
import requests
import time

import warnings
warnings.filterwarnings("ignore")

def get_critics_reviews(url):
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'lxml')
    reviews = soup.find_all("a", {"class": "tracked-offsite-link"})
    filter = ["Roger Ebert", "ReelViews", "Washington Post",
              "1,001 Movies Reviewed Before You Die", "1,001 Movies Reviewed Before You Die", "rogerebert.com",
              "New York Times"]
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

def get_user_reviews_selenium(url):

    list_reviews = []

    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(2)
    #driver.execute_script(f"location.href='{url}';")
    #selector = Select(driver.find_element_by_class_name('lister-sort-by'))
    selector = Select(driver.find_element(by=By.CLASS_NAME, value='lister-sort-by'))
    time.sleep(2)
    selector.select_by_visible_text('Review Rating')
    time.sleep(2)
    #driver.find_element_by_class_name('lister-sort-direction').click()
    driver.find_element(by=By.CLASS_NAME, value='lister-sort-direction').click()

    time.sleep(0.8)

    #for review in driver.find_elements_by_class_name('review-container'):
    for review in driver.find_elements(by=By.CLASS_NAME, value='review-container'):

        dictionary = {'title': review.find_element_by_class_name('title').text,
                      'content': review.find_element_by_class_name('show-more__control').text}
        list_reviews.append(dictionary)
        time.sleep(0.8)
    driver.close()
    return list_reviews



def get_user_reviews_bs(url):

    soup = BeautifulSoup(requests.get(url).text, 'lxml')

    time.sleep(0.8)

    list_reviews = []

    reviews = soup.find('div', {'class': 'lister-list'}).find_all('div')
    for review in soup.find_all('div',  {'class': 'lister-item-content'}):
        dictionary = {'title': review.find('a').text,
                      'content': review.find('div', {'class': 'text show-more__control'}).text}
        list_reviews.append(dictionary)
        time.sleep(0.8)
    return list_reviews
