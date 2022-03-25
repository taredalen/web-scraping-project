import json
import time, requests
from bs4 import BeautifulSoup

from imdb.get_reviews import get_reviews
from imdb.user_reviews import get_user_reviews

data = {}

request = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')

for film in range(0, 1): #0, 250

    time.sleep(0.8)

    dictionnaire = {}
    liste_genres = []

    soup = BeautifulSoup(request.text, 'lxml')
    filmes = soup.find('tbody', {'class': 'lister-list'}).find_all('tr')[film]

    link = 'https://www.imdb.com/' + filmes.find_all('td')[1].find('a').get('href')

    time.sleep(0.8)

    soup = BeautifulSoup(requests.get(link).text, 'lxml')

    name = soup.find('h1', {'data-testid': 'hero-title-block__title'}).text
    year = soup.find('span', {'class': 'sc-52284603-2 iTRONr'}).text
    rating = soup.find('span', {'class': 'sc-7ab21ed2-1 jGRxWM'}).text
    metascore = soup.find('span', {'class': 'score-meta'})
    original_name = soup.find('div', {'class': 'sc-dae4a1bc-0 gwBsXc'})

    if metascore is None:
        metascore = ''
    else:
        metascore = metascore.text

    if original_name is None:
        original_name = name
    else:
        original_name = original_name.text[16:]


    genres = soup.find('div', {'data-testid': 'genres'}).find_all('span', {'class': 'ipc-chip__text'})

    for genre in genres:
        liste_genres.append(genre.text)

    user_review_url = link + 'reviews?ref_=tt_ov_rt'
    critic_review_url = link + 'externalreviews?ref_=tt_ov_rt'

    dictionnaire['link'] = link
    dictionnaire['name'] = name
    dictionnaire['year'] = year.replace(')', '')
    dictionnaire['genre'] = ', '.join(liste_genres)
    dictionnaire['rating'] = rating
    dictionnaire['metascore'] = metascore
    dictionnaire['user review url'] = user_review_url
    dictionnaire['critic review url'] = critic_review_url
    dictionnaire['users reviews'] = get_user_reviews(user_review_url)
    dictionnaire['critics reviews'] = get_reviews(critic_review_url)

    data[original_name] = dictionnaire
    print(film)
    print(name)

with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent=1)