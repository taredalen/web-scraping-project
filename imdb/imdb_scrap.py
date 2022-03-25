import csv
import json
import time, requests
from bs4 import BeautifulSoup

request = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')

fieldnames = ['link', 'name', 'year', 'genre', 'rating', 'original name']
data = {}


for film in range(0, 3):
    time.sleep(2)

    dictionnaire = {}
    liste_genres = []

    soup = BeautifulSoup(request.text, 'lxml')
    filmes = soup.find('tbody', {'class': 'lister-list'}).find_all('tr')[film]
    name = filmes.find_all('td')[1].find('a').text

    link = 'https://www.imdb.com/' + filmes.find_all('td')[1].find('a').get('href')

    time.sleep(1)
    soup = BeautifulSoup(requests.get(link).text, 'lxml')
    year = soup.find('a', {'class': 'ipc-link ipc-link--baseAlt ipc-link--inherit-color sc-52284603-1 ifnKcw'}).text
    #name = soup.find('h1', {'class': 'sc-b73cd867-0 eKrKux'}).text
    rating = soup.find('span', {'class': 'sc-7ab21ed2-1 jGRxWM'}).text

    original_name = soup.find('div', {'class': 'sc-dae4a1bc-0 gwBsXc'})

    if original_name is None:
        original_name = name
    else:
        original_name = original_name.text[16:]

    genres = soup.find('div', {'data-testid': 'genres'}).find_all('span', {'class': 'ipc-chip__text'})

    for genre in genres:
        liste_genres.append(genre.text)

    dictionnaire['link'] = link
    dictionnaire['name'] = name
    dictionnaire['year'] = year.replace(')', '')
    dictionnaire['genre'] = ', '.join(liste_genres)
    dictionnaire['rating'] = rating

    data[original_name] = dictionnaire

with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent=1)