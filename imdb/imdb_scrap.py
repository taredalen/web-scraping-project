import csv
import time, requests
from bs4 import BeautifulSoup

request = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')

fieldnames = ['link', 'name', 'year', 'genre', 'rating', 'original name']
rows = []

liste_des_filmes = []

for film in range(0, 2):
    time.sleep(1)
    dictionnaire = {}

    soup = BeautifulSoup(request.text, 'lxml')
    filmes = soup.find('tbody', {'class': 'lister-list'}).find_all('tr')[film]

    link = 'https://www.imdb.com/' + filmes.find_all('td')[1].find('a').get('href')

    soup = BeautifulSoup(requests.get(link).text, 'lxml')

    year = soup.find('a', {'class': 'ipc-link ipc-link--baseAlt ipc-link--inherit-color sc-52284603-1 ifnKcw'}).text
    name = soup.find('h1', {'class': 'sc-b73cd867-0 eKrKux'}).text
    rating = soup.find('span', {'class': 'sc-7ab21ed2-1 jGRxWM'}).text
    original_name = soup.find('div', {'class': 'sc-dae4a1bc-0 gwBsXc'}).text[16:]

    liste_genres = []
    genres = soup.find('div', {'class': 'ipc-chip-list sc-14389611-4 ctpXmw'}).find_all('span', {'class': 'ipc-chip__text'})
    for genre in genres:
        liste_genres.append(genre.text)

    dictionnaire['link'] = link
    dictionnaire['name'] = name
    dictionnaire['year'] = year.replace(')', '')
    dictionnaire['genre'] = ', '.join(liste_genres)
    dictionnaire['rating'] = rating
    dictionnaire['original name'] = original_name

    rows.append(dictionnaire)

print(rows)


with open('imdb.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)