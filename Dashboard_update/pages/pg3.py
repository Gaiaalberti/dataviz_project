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


def line_italy():
    grouped_it = df_italy.groupby(["term"])["gender"].value_counts(normalize=True).unstack()
    grouped = grouped_it.reset_index()
    fig_it = px.line(x=grouped["term"], y=((grouped["female"])*100).round(2),
             labels=dict(x="Term", y="% of females MEPs"))
    fig_it.update_traces(line_color='pink', line_width=4)
    fig_it.update_layout(plot_bgcolor='#eeeeee', paper_bgcolor="#eeeeee")
    return fig_it

layout=dbc.Container([
    
    html.Div(style={'height':'20px'}),
    dbc.Row([
        html.H4(children="Italian female MEPs in the European Parliament", 
                style={'textAlign': 'left', "color" : "black", 'font-weight': 'bold'}),
        html.H6(children="Let's look at the progress made by Italy in increasing the percentage of italian female deputies in the EU "),
        html.Div(style={'height':'15px'}), 
        ]),
     
    dbc.Row([
        dbc.Col([dcc.Graph(figure=line_italy())],
                width={'size':8
                       , 'offset':0,
                       'order':1}),
        dbc.Col([
            html.H6(" Interestingly, between the seventh (2009-2014) and eighth term (2014-2019), there was not a significant increase in the percentage of women as one might expect, especially given the increased focus and discussion on gender equality in the last decade. Even if, there has been a progress  we are still far from achieving gender parity. This highlights the need for continued efforts to increase the representation of women in politics and address the persistent gender gap.",
                   style={'textAlign': 'center', "color" :"black"})],
            width={'size':4,'offset': 0 , "order":2 }
        )], align= "center" ),
    
    dbc.Row([
        html.H4(children = 'Gender gap for Italian MEPs per european group or national group across terms', 
                    style={'textAlign': 'left', "color" : "black", 'font-weight': 'bold'}
                    ),
        html.H6(children = '', 
                    style={'textAlign': 'left'}
                    ),       
        ]),
    html.Div(style={'height':'40px'}),    
    dbc.Row([    
        dbc.Col([
            dcc.Dropdown(id='drop1', multi=False, value='1979-1984',
                         options=[{'label':x, 'value':x} for x in df_italy['term'].unique()])
            ],width={'size':4, 'offset':2}),
        
        dbc.Col([

            dcc.Dropdown(id='drop2', multi=False, value='eu_group_1',
                         options=[
        {'label': 'National party', 'value': 'nation_group'},
        {'label': 'European group', 'value': 'eu_group_1'}
    ])
            ],width={'size':4})]),
 
    dbc.Row([
        dbc.Col([        
            dcc.Graph(id="bar_line11")
        
    ])
    ])
])


@callback(
    Output('bar_line11', 'figure'),
    [Input('drop1', 'value'),
     Input('drop2', 'value')])


def bar_line(drop1, drop2):

    dff_italy = df_italy[df_italy['term'] == drop1]
    # Group data by selected group
    if drop2 == 'nation_group':
        grouped_df = dff_italy.groupby(['nation_group', 'gender']).size().reset_index(name='count')
        grouped_df = grouped_df.sort_values(by='count', ascending=False)
        fig777 = px.bar(grouped_df, x="nation_group", y='count', color='gender',
                         barmode='stack',
                         color_discrete_map={'male': '#72B7B2', 'female': '#FF92A5'})
        fig777.update_layout(
            height=600,
            xaxis=dict(
                tickmode='array',
                ticktext=grouped_df['nation_group'].apply(lambda x: '<br>'.join(x.split())).tolist(),
                tickvals=grouped_df['nation_group'].tolist()
            ))
    else:
        grouped_df = dff_italy.groupby(['eu_group_1', 'gender']).size().reset_index(name='count')
        grouped_df = grouped_df.sort_values(by='count', ascending=False)
        fig777 = px.bar(grouped_df, x="eu_group_1", y='count', color='gender',
                         barmode='stack',
                         color_discrete_map={'male': '#72B7B2', 'female': '#FF92A5'},
                         )
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
    xaxis_title="Parties",
    yaxis_title='Number of Deputies',
    plot_bgcolor='#eeeeee', paper_bgcolor="#eeeeee",
    hoverlabel=dict(font=dict(color='white')))
    return fig777
        
    
 