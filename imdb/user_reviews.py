import time
import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.select import Select

import warnings
warnings.filterwarnings("ignore")

def get_user_reviews(url):

    list_reviews = []

    driver = webdriver.Firefox()
    driver.get(url)

    selector = Select(driver.find_element_by_class_name('lister-sort-by'))
    selector.select_by_visible_text('Review Rating')
    driver.find_element_by_class_name('lister-sort-direction').click()

    soup = BeautifulSoup(requests.get(url).text, 'lxml')

    time.sleep(0.8)

    for review in driver.find_elements_by_class_name('review-container'):

        dictionary = {'title': review.find_element_by_class_name('title').text,
                      'content': review.find_element_by_class_name('show-more__control').text}
        list_reviews.append(dictionary)
        time.sleep(0.8)
    driver.close()
    return list_reviews


