import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()


def get_user_reviews(url):

    driver.get(url)

    selector = Select(driver.find_element_by_class_name('lister-sort-by'))
    selector.select_by_visible_text('Review Rating')
    driver.find_element_by_class_name('lister-sort-direction').click()

    soup = BeautifulSoup(requests.get(url).text, 'lxml')

    time.sleep(0.8)

    dictionary = {}

    reviews = soup.find('div', {'class': 'lister-list'}).find_all('div')
    for review in soup.find_all('div',  {'class': 'lister-item-content'}):
        title = review.find('a').text
        content = review.find('div', {'class': 'text show-more__control'}).text

        print(title)
        print(content)

        dictionary['title'] = title
        dictionary['content'] = content

    print(dictionary)
    time.sleep(0.8)


    return dictionary

(get_user_reviews('https://www.imdb.com/title/tt0111161/reviews?sort=userRating&dir=desc&ratingFilter=0'))