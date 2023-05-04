# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 18:23:25 2023

@author: gaiaa
"""

import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd



dash.register_page(__name__, name='Italy')

df_italy = pd.read_csv("dataset/italy.csv")
#df = df[(df['country'] == 'Italy')]



layout=dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H3(children = 'EU parties in the top ten countries', 
                    style={'textAlign': 'center', "color" : "black"},
                    ), 
            
            dcc.Dropdown(id='drop1', multi=False, value='1979-1984',
                         options=[{'label':x, 'value':x} for x in df_italy['term'].unique()]),  

            dcc.Dropdown(id='drop2', multi=False, value='eu_group_1',
                         options=[
        {'label': 'National party', 'value': 'nation_group'},
        {'label': 'European group', 'value': 'eu_group_1'}
    ]),  
            
            dcc.Graph(id="bar_line11")
            
        ], width=12, align = "center"),
        
        ])])






@callback(
    Output('bar_line11', 'figure'),
    [Input('drop1', 'value'),
     Input('drop2', 'value')])


def bar_line(drop1, drop2):

    dff_italy = df_italy[df_italy['term'] == drop1]
    # Group data by selected group
    if drop2 == 'nation_group':
        grouped_df = dff_italy.groupby(['nation_group', 'gender']).size().reset_index(name='count')
        fig777 = px.bar(grouped_df, x="nation_group", y='count', color='gender',
                         barmode='stack',
                         color_discrete_map={'male': 'blue', 'female': 'pink'})
        fig777.update_layout(
            height=600,
            xaxis=dict(
                tickmode='array',
                ticktext=grouped_df['nation_group'].apply(lambda x: '<br>'.join(x.split())).tolist(),
                tickvals=grouped_df['nation_group'].tolist()
            ))
    else:
        grouped_df = dff_italy.groupby(['eu_group_1', 'gender']).size().reset_index(name='count')
        fig777 = px.bar(grouped_df, x="eu_group_1", y='count', color='gender',
                         barmode='stack',
                         color_discrete_map={'male': 'blue', 'female': 'pink'})
    # Create bar plot with Plotly
    
        fig777.update_layout(
            height=600,
            xaxis=dict(
                tickmode='array',
                ticktext=grouped_df['eu_group_1'].apply(lambda x: '<br>'.join(x.split())).tolist(),
                tickvals=grouped_df['eu_group_1'].tolist()
            ))
    fig777.update_xaxes(tickangle=0, 
                            automargin=True, 
                            tickfont=dict(size=10),
                            title=dict(text=drop2, font=dict(size=12)))
    fig777.update_layout(
    title=f'Members of the European Parliament for Italy',
    xaxis_title=drop1,
    yaxis_title='Number of Deputies')
    return fig777