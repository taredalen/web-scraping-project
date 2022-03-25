import warnings

warnings.filterwarnings("ignore")

import time, requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.select import Select

link = 'https://www.imdb.com//title/tt0111161/reviews?ref_=tt_ov_rt'

driver = webdriver.Firefox()
driver.get(link)
soup = BeautifulSoup(requests.get(link).text, 'lxml')


selector = Select(driver.find_element_by_class_name('lister-sort-by'))
selector.select_by_visible_text('Review Rating')
driver.find_element_by_class_name('lister-sort-direction').click()

time.sleep(0.8)

#driver.close()


for review in soup.find_all('div', {'class': 'review-container'}):
    title = soup.find('a', {'class': 'title'}).text
    content = soup.find('div', {'class': 'text show-more__control'}).text

    print(title)
    print(content)
