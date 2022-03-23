import time, requests
from bs4 import BeautifulSoup
from selenium import webdriver

request = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')
soup = BeautifulSoup(request.text, 'lxml')

fieldnames = ['name', 'year', 'genre', 'rating']
rows = []

liste_des_filmes = []

for film in range(0, 1):
    dictionnaire = {}

    filmes = soup.find("tbody", {"class": "lister-list"}).find_all('tr')[film]

    name = filmes.find_all('td')[1].find('a').text
    year = filmes.find_all('td')[1].find('span').text.replace('(', '')
    score = filmes.find_all('td')[2].find('strong').text
    genre = filmes.find_all('td')[2].find('strong').text
    rating = filmes.find_all('td')[2].find('strong').text

    dictionnaire['name'] = name
    dictionnaire['year'] = year.replace(')', '')
    rows.append(dictionnaire)


