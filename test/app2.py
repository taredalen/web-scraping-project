import dash
import json
import pandas as pd

from dash.dependencies import Input, Output

from data_function import *
from graph_function import *

<<<<<<< HEAD
# Load data

df = pd.read_csv('test/data/stockdata2.csv', index_col=0, parse_dates=True)
df.index = pd.to_datetime(df['Date'])

# Initialize the app
app2 = dash.Dash(__name__)
app2.config.suppress_callback_exceptions = True


import json
import pandas as pd
import seaborn as sns
from pandas import Series
import matplotlib.pyplot as plt

with open('Data/final_data.json', 'r') as f:
=======
app2 = dash.Dash(__name__)
app2.config.suppress_callback_exceptions = True

with open('../Data/final_data.json', 'r') as f:
>>>>>>> e7efa18ea5b103e742c08a14e51a277b6a9e68cd
    data = json.loads(f.read())

df_not_normalized = get_json_data()

df2 = pd.json_normalize(data, meta='title', record_path=['results'])

df2['year'] = df2['year'].astype(int)
df2['rating'] = pd.to_numeric(df2['rating'])
df2['metascore'] = pd.to_numeric(df2['metascore']) / 10
df2['rating sc'] = pd.to_numeric(df2['rating sc'])
df2 = df2[['title', 'year', 'rating', 'metascore', 'genre', 'rating sc', 'name french']]

app2.layout = html.Div(
    children=[
        html.Div(className='row',
                 children=[
                     html.Div(className='four columns div-user-controls',
                              children=[
                                  html.H2('DASH - MOVIES STATS'),
                                  html.P('Pick one or more components from the dropdown below.'),
                                  html.Div(
                                      className='div-for-dropdown',
                                      children=[
                                          dcc.Dropdown(
                                              id='dataselector',
                                              options=['IMDB-SC-Scores', 'Popular genre per decade', 'NLP'],
                                              value='IMDB-SC-Scores',
                                              style={'backgroundColor': '#1E1E1E'},
                                              className='stockselector'
                                          )
                                      ],
                                      style={'color': '#1E1E1E'}),
                                  html.P('Or you can also see stats for each decade by selecting.'),
                                  html.Div(
                                      className="div-for-dropdown",
                                      children=[
                                          dcc.Dropdown(
                                              id="decade-selector",
                                              options=['1930s', '1940s', '1950s', '1960s', '1970s',
                                                       '1980s', '1990s', '2000s', '2010s', '2020s'],
                                              value='1930s',
                                              placeholder="Select decade",
                                          )
                                      ],
                                  ),
                                  html.P('Or also see stats for each movie by search.'),
                                  html.Div(
                                      className="div-for-dropdown",
                                      children=[
                                          dcc.Dropdown(
                                              id="movie-selector",
                                              options=df2['title'],
                                              value='The Godfather'
                                          )
                                      ],
                                  ),
                                  html.Div(
                                      className="div-for-dropdown",
                                      children=[
                                          dcc.Graph(
                                              id='timeseries_third',
                                              config={'displayModeBar': False},
                                              animate=True)
                                      ],
                                  )
                              ]
                              ),
                     html.Div(className='eight columns div-for-charts bg-grey',
                              id='main',
                              children=[])
                 ])
    ]
)


# Callback for timeseries price
@app2.callback(Output('main', 'children'),
               [Input('dataselector', 'value')],
               #[Input('movie-selector', 'movie')]
               )
def update_timeseries(value):
    print(value)
<<<<<<< HEAD
    trace = []
    df_sub = df
    # STEP 2
    # Draw and append traces for each stock
    print(df2)
    trace.append(go.Scatter(x=df2['name french'],
                                 y=df2['year'],
                                 mode='lines',
                                 opacity=0.7,
                                 
                                 textposition='bottom center'))
    """
    for stock in df2['name french']:
        trace.append(go.Scatter(x=stock.index,
                                 y=df2['year'],
                                 mode='lines',
                                 opacity=0.7,
                                 name=stock,
                                 textposition='bottom center'))
    """
    # STEP 3
    traces = [trace]
    data = [val for sublist in traces for val in sublist]
    # Define Figure
    # STEP 4
    figure = {'data': data,
              'layout': go.Layout(
                  colorway=["#5E0DAC", '#FF4F00', '#375CB1', '#FF7400', '#FFF400', '#FF0056'],
                  template='plotly_dark',
                  paper_bgcolor='rgba(0, 0, 0, 0)',
                  plot_bgcolor='rgba(0, 0, 0, 0)',
                  margin={'b': 15},
                  hovermode='x',
                  autosize=True,
                  title={'text': 'Stock Prices', 'font': {'color': 'white'}, 'x': 0.5},
                  xaxis={'range': [df2.index.min(), df2.index.max()]},
              ),
              }
=======
    if value == 'IMDB-SC-Scores':
        figure = px.bar(
            df2, x='title', y=['rating', 'metascore', 'rating sc'], barmode='group',
            color_discrete_map={'rating': 'RebeccaPurple', 'metascore': 'MediumPurple', 'rating sc': 'MediumOrchid'},
            template="simple_white")
        figure.update_xaxes(rangeslider_visible=True)
        figure.update_xaxes(tickfont=dict(size=10))
        figure.update_layout(  # customize font and legend orientation & position
            legend=dict(title=None, orientation='h', y=1, yanchor='bottom', x=0.5, xanchor='center'),
            plot_bgcolor='#323130',
            paper_bgcolor='#323130',
            font=dict(color='white'),
            xaxis_title=None,
            yaxis_title=None,
            height=800,
            bargap=0.30
        )
        return dcc.Graph(id='timeseries', figure=figure)
>>>>>>> e7efa18ea5b103e742c08a14e51a277b6a9e68cd

    if value == 'Popular genre per decade':
        figure = px.bar(get_genre_by_decades(df2), x='decade', y='genre count', color='genre', barmode='group',
                        color_discrete_sequence=px.colors.qualitative.Vivid)
        figure.update_layout(  # customize font and legend orientation & position
            legend=dict(title=None, orientation='v'),
            plot_bgcolor='#323130',
            paper_bgcolor='#323130',
            font=dict(color='white'),
            xaxis_title=None,
            height=400,
        )
        figure.update_xaxes(tickfont=dict(size=10))
        figure.update_xaxes(rangeslider_visible=False)

        return html.Div(children=[
            dcc.Graph(id='timeseries',
                      figure=figure),
            dcc.Graph(id='timeseries_second',
                      config={'displayModeBar': False},
                      animate=True)
        ])

    #if value == 'NLP':  return html.Div(get_page_film(df_not_normalized, movie))




@app2.callback(Output('timeseries_second', 'figure'),
               [Input('decade-selector', 'value')])
def show_decade_genre(value):
    figure = px.bar(get_movies_by_decade(df2, value),
                    x='year', y='metascore', color='title', barmode='group',
                    color_discrete_sequence=px.colors.qualitative.Vivid)
    figure.update_xaxes(rangeslider_visible=False)
    figure.update_layout(
        legend=dict(title=None, orientation='v'),
        plot_bgcolor='#323130',
        paper_bgcolor='#323130',
        font=dict(color='white'),
        xaxis_title=None,
        yaxis_title=None,
        height=400
    )
    return figure


@app2.callback(Output('timeseries_third', 'figure'),
               [Input('movie-selector', 'value')])
def show_movie_score(value):
    figure = px.bar(
        get_movie_score(value), x='title', y=['metascore', 'rating sc', 'rating'], barmode='group',
        color_discrete_map={'rating': 'RebeccaPurple', 'metascore': 'MediumPurple', 'rating sc': 'MediumOrchid'},
        template="simple_white")
    figure.update_layout(
        legend=dict(title=None, orientation='v'),
        plot_bgcolor='#323130',
        paper_bgcolor='#323130',
        font=dict(color='white'),
        xaxis_title=None,
        yaxis_title=None,
        height=300,
        bargap=0.30
    )
    return figure


if __name__ == '__main__':
    app2.run_server(debug=True, threaded=True)
