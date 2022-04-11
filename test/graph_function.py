from dash import Dash, html, dcc
import plotly.express as px
import plotly
import plotly.graph_objs as go
import random


def get_page_film(list_film, film_name):
    film = next((dictionary for dictionary in list_film if dictionary["title"] == film_name), None)
    if film is not None:
        film_result = film['results'][0]
        adj_user_wordcloud = get_wordcloud(film_result["users reviews"], "USERS MOST USED ADJECTIVES")
        adj_pro_wordcloud = get_wordcloud(film_result["critics reviews"], "CRITICS MOST USED ADJECTIVE")
        adj_sc_workcloud = get_wordcloud(film_result["reviews sc"], "SENSCRITIQUE USERS MOST USED ADJECTIVES")
        return [html.P(" "), adj_user_wordcloud, adj_pro_wordcloud, adj_sc_workcloud]


def get_wordcloud(reviews, title):
    adj = []
    for review in reviews:
        for adjective in review['nlp']['most used adj']:
            adj.append(adjective)
    adj = sorted(adj, key=lambda x: x[0])

    adj = wordcount(adj)
    adj = sorted(adj, key=lambda x: x[1], reverse=True)
    words = [word for word, _ in adj]
    weights = [count * 8 for _, count in adj]
    # weights = [random.randint(15, 35) for i in range(30)]
    if len(words) > 30:
        words = words[:30]
        weights = weights[:30]
    colors = [plotly.colors.DEFAULT_PLOTLY_COLORS[random.randrange(1, 10)] for i in range(len(words))]
    data = go.Scatter(x=[random.random() for i in range(len(words))],
                      y=[random.random() for i in range(len(words))],
                      mode='text',
                      text=words,
                      marker={'opacity': 0.3},
                      textfont={'size': weights,
                                'color': colors}
                      )

    layout = go.Layout({'xaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False},
                        'yaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False}})

    fig = go.Figure(data=[data], layout=layout)
    fig.update_layout(
        #title_text=title,
        title={
            'text': title,
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        #legend=dict(title=None, orientation='v',  yanchor='bottom', x=0.5, xanchor='center'),
        plot_bgcolor='#323130',
        paper_bgcolor='#323130',
        font=dict(color='white'),
        xaxis_title=None,
        yaxis_title=None
    )
    return dcc.Graph(figure=fig, style={'height': '100vh'})


def wordcount(list_word):
    wordcount_list = []

    current_word = None
    current_count = 0

    for word, count in list_word:
        if current_word == word:
            current_count += count
        else:
            if current_word is not None:
                wordcount_list.append((current_word, current_count))
            current_word = word
            current_count = count
    return wordcount_list