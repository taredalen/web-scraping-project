import time

dictionnaire = {}

def get_movies(movies):
    for i in movies:
        time.sleep(2)
        film_name = i.find_element_by_tag_name('a').text
        print(film_name)
        dictionnaire['name'] = film_name
