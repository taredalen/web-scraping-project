import time


def get_movies(movies):
    for i in movies:
        time.sleep(2)
        x = i.find_element_by_tag_name('a').text
        print(x)