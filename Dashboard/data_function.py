import json
import pandas as pd
from pandas import Series

def get_json_data():
    with open('../Data/final_data.json', 'r') as f:
        return json.loads(f.read())

def normalize_data():
    data = get_json_data()
    df = pd.json_normalize(data, meta='title', record_path=['results'])

    df['year'] = df['year'].astype(int)
    df['rating'] = pd.to_numeric(df['rating'])
    df['metascore'] = pd.to_numeric(df['metascore'])/10
    df['rating sc'] = pd.to_numeric(df['rating sc'])
    df['decade'] = (10 * (df['year'] // 10)).astype(str) + 's'
    return df[['title', 'year', 'rating', 'metascore', 'genre', 'rating sc', 'decade', 'country']]

def get_genre_by_decades():

    df = normalize_data()

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

def get_movies_by_decade(decade):

    df = normalize_data()

    index_decades = df[df['decade'] != decade].index

    df.drop(index_decades, inplace=True)

    s = df['genre'].str.split(' ').apply(Series, 1).stack()
    s.index = s.index.droplevel(-1)
    s.name = 'genre'
    del df['genre']
    df2 = df.join(s)
    return df2

def get_movie_score(title):
    df = normalize_data()
    index_title = df[df['title'] != title].index
    df.drop(index_title, inplace=True)
    return df

def get_movies_count_by_decade():
    df = normalize_data()
    df = df.groupby(['decade'], sort=True)['decade'].count()
    return df

def get_countries():
    df = normalize_data()
    s = df['country'].str.split(', ').apply(Series, 1).stack()
    s.index = s.index.droplevel(-1)
    s.name = 'country'
    del df['country']
    df2 = df.join(s)

    df = df2.groupby(['country'], sort=True)['country'].count()
    df = df.to_frame(name='country count').reset_index()
    return df