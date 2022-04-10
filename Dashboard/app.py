from distutils.log import debug
from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
import json
from pandas import Series
import plotly
import plotly.graph_objs as go
import random

from pandas.io.json import json_normalize
from data_function import *
from graph_function import *
   
# visit http://127.0.0.1:8050/ in your web browser.

df_not_normalized = get_json_data()
df = normalize_data(df_not_normalized)
df_decade = get_genre_by_decades(df)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)


"""
def get_graph_for_film(film_name):
    for film in df:
        if film['title'] == film_name:
            info = get_info_film(film)
            film_result = film['results'][0]
            adj_user_wordcloud = get_word_cloud(film_result["users reviews"], "Users most used adjective")
            adj_pro_wordcloud = get_word_cloud(film_result["critics reviews"], "Critics most used adjective")
            return [info, adj_user_wordcloud, adj_pro_wordcloud]

def get_info_film(film):
    info = "Title: " + film["title"] + " Year: " + film["results"][0]["year"] + " Genre: " + film["results"][0]["genre"]
    return html.Div(info )

def get_word_cloud(user_review, title):
    user_adj = []
    for review in user_review:
        for adj in review['nlp']['most used adj']:
            user_adj.append(adj)
    user_adj = sorted(user_adj, key=lambda x: x[0])

    user_adj = wordcount(user_adj)
    user_adj = sorted(user_adj, key=lambda x: x[1], reverse=True)
    words = [word for word, _ in user_adj]
    weights = [count*8 for _, count in user_adj]

    colors = [plotly.colors.DEFAULT_PLOTLY_COLORS[random.randrange(1, 10)] for i in range(len(words))]
    data = go.Scatter(x=[random.random() for i in range(len(words))],
                 y=[ random.random() for i in range(len(words))],
                 mode='text',
                 text=words[:30],
                 marker={'opacity': 0.3}, 
                 textfont={'size': weights[:30],
                           'color': colors})
    layout = go.Layout({'xaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False},
                    'yaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False}})
    
    fig = go.Figure(data=[data], layout=layout)
    fig.update_layout(title_text=title)

    return dcc.Graph(figure=fig, style={'height':'100vh'})

def wordcount(list_word):
    wordcount_list = []

    current_word = None
    current_count = 0

    for word, count in list_word:
        if current_word == word:
            current_count += count
        else :
            wordcount_list.append((current_word, current_count))
            current_word = word
            current_count = count

    return wordcount_list




"""

app.layout = html.Div([
    html.H1("Dashboard"),
    #html.Div(),
    dcc.Input(id="search-film", type="text"),
    html.Button(id="submit-film", children="submit"),
    html.Div(id="main-page", children=get_menu_graph(df, df_decade))

]
)

@app.callback(
    Output("main-page", "children"),
    Input("submit-film", "n_clicks"),
    State("search-film", "value")
)
def update_page(n_clicks, value):
    if value is None or len(value) == 0:
        return get_menu_graph(df, df_decade)
    elif value in df['title'].values:
        return html.Div(get_page_film(df_not_normalized, value))
    else:
        return html.H1("Pas Trouvé")


if __name__ == '__main__':
    app.run_server(debug=True)