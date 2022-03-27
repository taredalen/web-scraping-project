from bs4 import BeautifulSoup
import requests
import json
import time
import re

from imdb.reviews import get_critics_reviews, get_user_reviews_bs

start = time.time()
print('starting')

film_rows = []

request = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')

for film in range(0, 100):

    time.sleep(0.8)

    list_genre = []

    soup = BeautifulSoup(request.text, 'lxml')
    filmes = soup.find('tbody', {'class': 'lister-list'}).find_all('tr')[film]

    link = 'https://www.imdb.com/' + filmes.find_all('td')[1].find('a').get('href')

    time.sleep(0.8)

    soup = BeautifulSoup(requests.get(link).text, 'lxml')

    name = soup.find('h1', {'data-testid': 'hero-title-block__title'})
    year = soup.find('span', {'class': 'sc-52284603-2 iTRONr'})
    rating = soup.find('span', {'class': 'sc-7ab21ed2-1 jGRxWM'})
    metascore = soup.find('span', {'class': 'score-meta'})
    original_name = soup.find('div', {'class': 'sc-dae4a1bc-0 gwBsXc'})

    budget = soup.find('section', {'cel_widget_id': 'StaticFeature_BoxOffice'}).find('span', {'class': 'ipc-metadata-list-item__list-content-item'})
    gross = soup.find('section', {'cel_widget_id': 'StaticFeature_BoxOffice'}).find('span', {'class': 'ipc-metadata-list-item__list-content-item'})

    if budget is None or gross is None:
        income = ''
    else:
        gross = ''.join(re.findall(r'\b\d+\b', gross.text))
        budget = ''.join(re.findall(r'\b\d+\b', budget.text))

        result = int(gross) - int(budget)
        income = str(result)

    if metascore is None:
        metascore = ''
    else:
        metascore = metascore.text

    if original_name is None:
        original_name = name.text
    else:
        original_name = original_name.text[16:]

    genres = soup.find('div', {'data-testid': 'genres'}).find_all('span', {'class': 'ipc-chip__text'})

    for genre in genres:
        list_genre.append(genre.text)

    user_review_url = link + 'reviews?ref_=tt_ov_rt'
    critic_review_url = link + 'externalreviews?ref_=tt_ov_rt'

    dictionary = {'link': link,
                  'year': year.text.replace(')', ''),
                  'genre': ' '.join(list_genre),
                  'rating': rating.text,
                  'income': income,
                  'metascore': metascore,
                  'user review url': user_review_url,
                  'critic review url': critic_review_url,
                  'users reviews': get_user_reviews_bs(link+'reviews?sort=userRating&dir=asc&ratingFilter=0'),
                  'critics reviews': get_critics_reviews(critic_review_url)}

    film_data = {'title': original_name, 'results': [dictionary]}

    print('{} {}'.format(film, original_name))
    film_rows.append(film_data)

with open('data.json', 'w') as outfile:
    json.dump(film_rows, outfile, indent=1)


def convert(seconds):
    return time.strftime("%H:%M:%S", time.gmtime(seconds))

print("{}".format(convert(time.time() - start)))