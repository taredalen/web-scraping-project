import json
import pandas as pd
from pandas import Series

with open('../Data/final_data.json', 'r') as f:
    data = json.loads(f.read())

df = pd.json_normalize(data, meta='title', record_path=['results'])


def get_json_data():
    with open('../Data/data_imdb_nlp.json', 'r') as f:
        return json.loads(f.read())

def normalize_data():
    df['year'] = df['year'].astype(int)
    df['rating'] = pd.to_numeric(df['rating'])
    df['metascore'] = pd.to_numeric(df['metascore'])/10
    df["rating sc"] = pd.to_numeric(df["rating sc"])
    return df[['title', 'year', 'rating', 'metascore', 'genre', 'rating sc']]

def get_genre_by_decades(df_c):

    df = df_c[['title', 'year', 'metascore', 'rating', 'genre']]

    s = df['genre'].str.split(' ').apply(Series, 1).stack()
    s.index = s.index.droplevel(-1)
    s.name = 'genre'
    del df['genre']
    df2 = df.join(s)

    df2 = df2.groupby(['year', 'genre'], sort=True)['year'].count()
    df_year = df2.to_frame(name='genre count').reset_index()

    df_year['decade'] = (10 * (df_year['year'] // 10)).astype(str) + 's'

    df_dec = df_year.groupby(['decade', 'genre'], sort=True)['year'].count()
    df_dec = df_dec.to_frame(name='genre count').reset_index()

    return df_dec

def get_movies_by_decade(df, decade):

    df['year'] = df['year'].astype(int)
    df['rating'] = pd.to_numeric(df['rating'])
    df['metascore'] = pd.to_numeric(df['metascore']) / 10
    df['decade'] = (10 * (df['year'] // 10)).astype(str) + 's'

    df = df[['title', 'year', 'rating', 'metascore', 'genre', 'decade']]

    index_decades = df[df['decade'] != decade].index

    df.drop(index_decades, inplace=True)

    s = df['genre'].str.split(' ').apply(Series, 1).stack()
    s.index = s.index.droplevel(-1)
    s.name = 'genre'
    del df['genre']
    df2 = df.join(s)
    return df2

def get_movie_score(title):
    df = pd.json_normalize(data, meta='title', record_path=['results'])

    df['rating'] = pd.to_numeric(df['rating'])
    df['rating sc'] = pd.to_numeric(df['rating sc'])
    df['metascore'] = pd.to_numeric(df['metascore']) / 10

    df = df[['title', 'rating', 'metascore', 'rating sc']]

    index_title = df[df['title'] != title].index
    df.drop(index_title, inplace=True)

    return df
    