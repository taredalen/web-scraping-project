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