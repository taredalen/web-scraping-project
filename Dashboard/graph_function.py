from dash import Dash, html, dcc
import plotly.express as px
import plotly
import plotly.graph_objs as go
import random
import sys, os
sys.path.insert(0, str(os.getcwd()) + '/Dashboard')
from data_function import get_movies_by_decade

def get_menu_graph(dataframe, dataframe_decade):
    
    return html.Div(children=[
        dcc.Graph(id="rating-graph", 
        figure=px.bar(dataframe, x="title", y=['rating', 'metascore', 'rating sc'], barmode='group', title="User rating and metascore"), 
        style={'width': '210vh', 'height': '100vh'}),
        dcc.Graph(id="movie-count-graph", 
        figure=px.bar(get_movies_by_decade(dataframe), x="decade", labels={
            'decade': 'movies',
            'index': 'decade'
        })),
        dcc.Graph(id="genre-graph", 
        figure=px.bar(dataframe_decade, x="decade", y="genre count", color='genre', barmode="group", title="Popular genre per decade"))
    ])

def get_page_film(list_film, film_name):
    film = next((dictionary for dictionary in list_film if dictionary["title"] == film_name), None)
    if film is not None:
        info = get_film_info(film)
        film_result = film['results'][0]
        adj_user_wordcloud = get_wordcloud(film_result["users reviews"], "Users most used adjectives")
        adj_pro_wordcloud = get_wordcloud(film_result["critics reviews"], "Critics most used adjectives")
        adj_sc_workcloud = get_wordcloud(film_result["reviews sc"], "Senscritique users most used adjectives")
        return [info, get_ratings(film),  adj_user_wordcloud, adj_pro_wordcloud, adj_sc_workcloud]

def get_ratings(film):
    fig = go.Figure(data=[
        go.Bar(name="user rating", y=[float(film["results"][0]["rating"])]),
        go.Bar(name="metascore", y=[float(film["results"][0]["metascore"])/10]),
        go.Bar(name="Senscritique rating", y=[float(film["results"][0]["rating sc"])])
    ])
    return dcc.Graph(id='rating-movie-graph',
    figure=fig, style={"width": "150vh"})

def get_film_info(film):
    info = "Title: " + film["title"] + " Year: " + film["results"][0]["year"] + " Genre: " + film["results"][0]["genre"]
    return html.Div(info )

"""
renvoie les 30 adjectifs les plus utilisé sous formes de wordcloud
"""
def get_wordcloud(reviews, title):
    adj = []
    for review in reviews:
        for adjective in review['nlp']['most used adj']:
            adj.append(adjective)
    adj = sorted(adj, key=lambda x: x[0])

    adj = wordcount(adj)
    adj = sorted(adj, key=lambda x: x[1], reverse=True)
    words = [word for word, _ in adj]
    weights = [count*8 for _, count in adj]
    #weights = [random.randint(15, 35) for i in range(30)]
    if len(words) > 30: 
        words = words[:30]
        weights = weights[:30]
    colors = [plotly.colors.DEFAULT_PLOTLY_COLORS[random.randrange(1, 10)] for i in range(len(words))]
    data = go.Scatter(x=[random.random() for i in range(len(words))],
                 y=[ random.random() for i in range(len(words))],
                 mode='text',
                 text=words,
                 marker={'opacity': 0.3}, 
                 textfont={'size': weights,
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
            if current_word is not None:
                wordcount_list.append((current_word, current_count))
            current_word = word
            current_count = count
    return wordcount_list