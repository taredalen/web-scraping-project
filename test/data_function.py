import json
import pandas as pd
from pandas import Series

def get_json_data():
    with open('../Data/data3.json', 'r') as f:
        return json.loads(f.read())

def normalize_data(data):
    df = pd.json_normalize(data, meta='title', record_path=['results'])

    df['year'] = df['year'].astype(int)
    df['rating'] = pd.to_numeric(df['rating'])
    df['metascore'] = pd.to_numeric(df['metascore'])/10
    return df[['title', 'year', 'rating', 'metascore', 'genre']]

def get_genre_by_decades(df_c):
    s = df_c['genre'].str.split(' ').apply(Series, 1).stack()
    s.index = s.index.droplevel(-1)
    s.name = 'genre'
    del df_c['genre']
    df2 = df_c.join(s)

    df2 = df2.groupby(['year', 'genre'], sort=True)['year'].count()
    df_year = df2.to_frame(name = 'genre count').reset_index()

    df_year['decade'] = (10 * (df_year['year'] // 10)).astype(str) + 's'

    df_dec = df_year.groupby(['decade', 'genre'], sort=True)['year'].count()
    df_dec = df_dec.to_frame(name = 'genre count').reset_index()
    return df_dec