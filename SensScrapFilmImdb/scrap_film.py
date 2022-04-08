from bs4 import BeautifulSoup
import requests
import time
import json


def get_all_film_from_json(dict_film):
    url = "https://www.senscritique.com/search?q="

    list_movie_sens_link = []
    
    for film in dict_film:
        time.sleep(0.8)
        req = requests.get(url + film["title"].replace(" ", "%20"))
        soup = BeautifulSoup(req.text, 'lxml')

        link = soup.find("div", {"class": "ProductListItem__TextContainer-sc-1ci68b-8 kKuZab"}).find('a').get("href")
        if film["title"] == "Gisaengchung": link = "https://www.senscritique.com/film/parasite/25357970"
        list_movie_sens_link.append((film['title'], link))


    return list_movie_sens_link


def get_data_on_film(list_link):
    list_movies = []
    for title, url in list_link:
        time.sleep(0.8)
        url_reviews = url + "/critiques"
        reviews = get_reviews(url_reviews)
        score = get_score(url)
        dictionary = {"rating sc": score, "reviews sc": reviews, "link sc": url}
        list_movies.append({"title": title, "results": [dictionary]})
    
    return list_movies


def get_reviews(url):
    reviews_list = []
    print(url)

    req = requests.get(url)

    soup = BeautifulSoup(req.text, "lxml")

    list_review = soup.find_all("p", {"class": "ere-review-excerpt"})
    list_review_link = [link.find("a", {"class": "ere-review-anchor"}).get("href") for link in list_review]
    
    for link in list_review_link:
        time.sleep(0.8)
        print("https://www.senscritique.com" + link)
        req = requests.get("https://www.senscritique.com" + link)
        soup = BeautifulSoup(req.text, "lxml")
        title = soup.find("h1", {"class": "rvi-cover-title"}).text
        content = ' '.join(map(lambda x:x.text, soup.find("div", {"class": "rvi-review-content"}).find_all("p")))

        reviews_list.append({"title": title, "content": content})

    return reviews_list


def get_score(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")

    return soup.find("span", {"itemprop": "ratingValue"}).text


f = open("SensScrapFilmImdb/data.json")
data = json.load(f)

links = get_all_film_from_json(data)

list_movie_data = get_data_on_film(links)

with open("SensScrapFilmImdb/data_sc.json", 'w') as f:
    json.dump(list_movie_data, f, indent=1)