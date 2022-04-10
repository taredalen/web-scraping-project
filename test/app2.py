import dash
# import dash_html_components as html
# import dash_core_components as dcc
import plotly.graph_objects as go
from dash.dependencies import Input, Output

from data_function import *
from graph_function import *

# Load data

df = pd.read_csv('data/stockdata2.csv', index_col=0, parse_dates=True)
df.index = pd.to_datetime(df['Date'])

# Initialize the app
app2 = dash.Dash(__name__)
app2.config.suppress_callback_exceptions = True


import json
import pandas as pd
import seaborn as sns
from pandas import Series
import matplotlib.pyplot as plt

with open('../Data/final_data.json', 'r') as f:
    data = json.loads(f.read())

df2 = pd.json_normalize(data, meta='title', record_path=['results'])

df2['year'] = df2['year'].astype(int)
df2['rating'] = pd.to_numeric(df2['rating'])
df2['metascore'] = pd.to_numeric(df2['metascore'])/10
df2['rating sc'] = pd.to_numeric(df2['rating sc'])
df2 = df2[['title','year', 'rating', 'metascore', 'genre', 'rating sc','name french']]

def get_options(list_stocks):
    dict_list = []
    for i in list_stocks:
        dict_list.append({'label': i, 'value': i})
    print(dict_list)
    return dict_list


app2.layout = html.Div(
    children=[
        html.Div(className='row',
                 children=[
                    html.Div(className='four columns div-user-controls',
                             children=[
                                 html.H2('DASH - MOVIES STATS'),
                                 html.P('Visualising time series with Plotly - Dash.'),
                                 html.P('Pick one or more components from the dropdown below.'),
                                 html.Div(
                                     className='div-for-dropdown',
                                     children=[
                                         dcc.Dropdown(id='dataselector', options=['IMDB', 'SensCritique'],

                                                      style={'backgroundColor': '#1E1E1E'},
                                                      className='stockselector'
                                                      ),
                                     ],
                                     style={'color': '#1E1E1E'}),
                                 html.P('Or you can also see stats for each movie by selecting.'),

                                 #html.Div(
                                 #    className='div-for-dropdown',
                                 #    children=[
                                 #        dcc.Dropdown(id='filmselector', options=get_options(df2['name french'].unique()),
                                 #                     multi=True, value=[df['name french']],
                                 #                     style={'backgroundColor': '#1E1E1E'},
                                 #                     className='stockselector'
                                 #                     ),
                                 #    ],
                                 #    style={'color': '#1E1E1E'}),
                                ]
                             ),
                    html.Div(className='eight columns div-for-charts bg-grey',
                             children=[
                                 dcc.Graph(id='timeseries',
                                     config={'displayModeBar': False},
                                     animate=True),

                                  #dcc.Graph(id='change',
                                  #   config={'displayModeBar': False},
                                  #   animate=True)
                             ])
                    ])
        ]

)


# Callback for timeseries price
@app2.callback(Output('timeseries', 'figure'),
              [Input('dataselector', 'value')])
def update_timeseries(value):
    ''' Draw traces of the feature 'value' based one the currently selected stocks '''
    # STEP 1
    print(value)
    trace = []
    df_sub = df
    # STEP 2
    # Draw and append traces for each stock
    for stock in df2['name french']:
        trace.append(go.Scatter(x=stock.index,
                                 y=df2['year'],
                                 mode='lines',
                                 opacity=0.7,
                                 name=stock,
                                 textposition='bottom center'))
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

    return figure


'''def update_output(value):
    if value == 'IMDB':
        print(value)
        figure = px.bar(df2, x="title", y=['rating', "metascore"], barmode='group',
                        title="User rating and metascore")
        return figure
    
'''


'''@app2.callback(Output('change', 'figure'),
              [Input('stockselector', 'value')])
def update_change(selected_dropdown_value):
   #Draw traces of the feature 'change' based one the currently selected stocks 
    trace = []
    df_sub = df
    # Draw and append traces for each stock
    for stock in selected_dropdown_value:
        trace.append(go.Scatter(x=df_sub[df_sub['stock'] == stock].index,
                                 y=df_sub[df_sub['stock'] == stock]['change'],
                                 mode='lines',
                                 opacity=0.7,
                                 name=stock,
                                 textposition='bottom center'))
    traces = [trace]
    data = [val for sublist in traces for val in sublist]
    # Define Figure
    figure = {'data': data,
              'layout': go.Layout(
                  colorway=["#5E0DAC", '#FF4F00', '#375CB1', '#FF7400', '#FFF400', '#FF0056'],
                  template='plotly_dark',
                  paper_bgcolor='rgba(0, 0, 0, 0)',
                  plot_bgcolor='rgba(0, 0, 0, 0)',
                  margin={'t': 50},
                  height=250,
                  hovermode='x',
                  autosize=True,
                  title={'text': 'Daily Change', 'font': {'color': 'white'}, 'x': 0.5},
                  xaxis={'showticklabels': False, 'range': [df_sub.index.min(), df_sub.index.max()]},
              ),
              }

    return figure'''



if __name__ == '__main__':
    app2.run_server(debug=True,threaded = True)


