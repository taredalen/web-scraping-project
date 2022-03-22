
from selenium import webdriver
import time
import movies_func

driver = webdriver.Firefox()
driver.get("https://www.imdb.com/search/title/?groups=top_250&sort=user_rating")
#time.sleep(2)





for i in range(0,4):
    movies = driver.find_elements_by_class_name("lister-item-header")
    movies_func.get_movies(movies)
    driver.find_element_by_class_name("next-page").click()



driver.close()



