# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 18:23:21 2023

@author: gaiaa
"""

import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import base64
from PIL import Image
from dash import dcc, html, callback, Output, Input
# import networkx as nx
# import plotly.express as px
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
dname = dname.replace("\\", "/")
os.chdir(dname)


dash.register_page(__name__, name='Gender Gap')

# page 2 data
df = pd.read_csv("dataset/merged_coalition.csv")

def bar_line():
    grouped = df.groupby(["term"])["gender"].value_counts(normalize=True).unstack()
    grouped = grouped.reset_index()
    fig2 = px.line(x=grouped["term"], y=(grouped["female"])*100,#color=px.Constant("Trend"),
             labels=dict(x="Term", y="% of females MEPs")) #color="Legend"
    fig2.update_traces(line_color='black', line_width=2)
    fig2.add_bar(x=grouped["term"], y=(grouped["female"])*100, name="% of female MEPs",
            marker_color='#FF92A5')
            #hovertemplate = f'Term={grouped["term"]}<br>% of female MEPS={grouped["female"]}<extra></extra>',
            #hoverlabel=dict(bgcolor = "black"))
    fig2.update_layout(plot_bgcolor='#eeeeee', paper_bgcolor="#eeeeee")
    return fig2

    
    
layout=dbc.Container([

    dbc.Row([
        dbc.Col([
            html.H4(children = 'Gender Gap in the European Parliament thoruoghout the terms (1979-2024)', 
                    style={'textAlign': 'left', "color" : "black", 'font-weight': 'bold'},
                    className=' mb-4'),
            html.H6("Over the years, there has been a growing awareness of the gender gap and the need to address it in various fields, including politics. Political parties and organizations have made commitments to increase the representation of women in decision-making positions as we can see from the upward trend of the graph below."
            )], width=12)]),  
    
    dbc.Row([
        dbc.Col([dcc.Graph(figure=bar_line())],
                width={'size':8
                       , 'offset':0,
                       'order':1}),
        dbc.Col([
            html.P(" Interestingly, between the seventh (2009-2014) and eighth term (2014-2019), there was not a significant increase in the percentage of women as one might expect, especially given the increased focus and discussion on gender equality in the last decade. Even if, there has been a progress  we are still far from achieving gender parity. This highlights the need for continued efforts to increase the representation of women in politics and address the persistent gender gap.",
                   style={"color" :"black"})],
            width={'size':4,'offset': 0 , "order":2 }
        )], align= "center"
),
    html.Div(style={'height':'30px'}),
    
    

    dbc.Row([
        dbc.Col([
            html.H4(children = 'Female MEPs representation from each country thoruoghout the terms (1979-2024)', 
                    style={'textAlign': 'left', "color" : "black", 'font-weight': 'bold'},
                    className=' mb-4'),
            html.H6("Over the years, there has been a growing awareness of the gender gap and the need to address it in various fields, including politics. Political parties and organizations have made commitments to increase the representation of women in decision-making positions as we can see from the upward trend of the graph below."
            )], width=12)]),


    html.Div(style={'height':'20px'}),
    
    
    
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(id='dpdn', multi=False, value='1979-1984',
                         options=[{'label':x, 'value':x} for x in df['term'].unique()])], width={'size':5})
                         ]), 
    
    html.Div(style={'height':'20px'}),
    
    dbc.Row([
        dbc.Col([        
            dcc.Graph(id = "map")
        ],width={'size':5, 'offset':0,'order':1}),

        dbc.Col([
            dcc.Graph(id = "bar")
        ],width={'size':5, 'offset':2,'order':2}),

    html.Div(style={'height':'60px'}),
    
    ]),
    
    
    
    
    dbc.Row([
        dbc.Col([
            html.H4('The progess in gender equality in each country', 
                    style={'textAlign': 'left', "color" : "black", 'font-weight': 'bold'}),
            html.H6("The visualization below allows us understand whether there has been a costant upward positive trend for gender parity in each country or whether there are has been a decrease in women representation during specific periods"
           )], width=12)]),    
    
    html.Div(style={'height':'20px'}),
    
     dbc.Row([
         dbc.Col([
            dcc.Dropdown(id='drp_country', multi=False, value='France',
                         options=[{'label':x, 'value':x} for x in df['country'].unique()])]
            , width={'size':5})]),  

    dbc.Row([
         dbc.Col([            
            dcc.Graph(id="bar_line1", )
            
        ], width=7), #align = "end"
        
        dbc.Col(
            html.Div(children="descriptionnnnn......", 
                     style={'textAlign': 'center'}), width={'size':5}, align = "center"
        
        )],className=' mb-4'),
    
    html.Div(style={'height':'100px'}),


   
])




    
@callback(
    Output('bar_line1','figure'),
    Input('drp_country', 'value'))

def update_chart(drop):
    dff = df[df["country"] == drop]
    grouped = dff.groupby(['term', 'gender']).size().reset_index(name='counts')
    pivoted = grouped.pivot(index='term', columns='gender', values='counts')
    pivoted = pivoted.div(pivoted.sum(axis=1), axis=0)
    pivoted = pivoted.reindex(pivoted.sum(axis=1).sort_values(ascending=False).index)
    fig_1 = px.bar(pivoted, barmode='stack', orientation='h',color_discrete_map={"female": "#FF92A5", "male": "#72B7B2"})
    fig_1.update_layout( plot_bgcolor='#eeeeee', paper_bgcolor="#eeeeee", hoverlabel=dict(font=dict(color='white')))
    return fig_1 #legend=dict(x=0, y=-0.5, orientation='v'),

#def update_chart(drop):
#    dff = df[df['country'] == drop]
#    grouped = dff.groupby(['term', 'gender']).size().reset_index(name='counts')
#    pivoted = grouped.pivot(index='term', columns='gender', values='counts')
#    pivoted = pivoted.reindex(pivoted.sum(axis=1).sort_values(ascending=False).index)
    # take only the first 10 rows of pivoted
#    pivoted = pivoted.iloc[:10, :]
    # I want to invert the order of the rows
#    pivoted = pivoted.iloc[::-1]
 #   pivoted = pivoted.div(pivoted.sum(axis=1), axis=0)
 #   fig_1 = px.bar(pivoted.iloc[:10, :], barmode='stack', orientation='h',color_discrete_map={"female": "#FF92A5", "male": "#72B7B2"})
#    fig_1.update_layout(legend=dict(x=0, y=-0.5, orientation='h'), plot_bgcolor='#eeeeee', paper_bgcolor="#eeeeee")
#    return fig_1

@callback(
    Output('map','figure'),
    Input('dpdn', 'value'))

def update_graph(dpdn):
    dff = df[df['term'] == dpdn]
    grouped = dff.groupby(["country"])["gender"].value_counts(normalize=True).unstack().reset_index()
    fig = px.choropleth(grouped, locations = "country", locationmode="country names", color="female" , scope= "europe", hover_name="country", color_continuous_scale = "Burgyl", range_color=[0,1])
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, height=400, # increase the height of the chart
                  width=655, coloraxis_colorbar=dict(
        xanchor='left',
        len=0.8,
        yanchor='middle',
        y=0.5,
        thickness=18,
        tickfont=dict(size=15)))
    fig.update_layout(plot_bgcolor='#eeeeee', paper_bgcolor="#eeeeee")
    return fig


@callback(
    Output('bar','figure'),
    Input('dpdn', 'value'))

def update_bar(dpdn):
    dff = df[df['term'] == dpdn]
    grouped = dff.groupby(['orientation', 'gender']).size().reset_index(name='counts')
    pivoted2 = grouped.pivot(index='orientation', columns='gender', values='counts')
    pivoted2 = pivoted2.reindex(pivoted2.sum(axis=1).sort_values(ascending=False).index)
    pivoted2 = pivoted2.div(pivoted2.sum(axis=1), axis=0)
    pivoted2 = pivoted2.reindex(['left', 'centre-left', 'centre', 'centre-right', 'right', 'Non aligned'])
    fig_bar = px.bar(pivoted2.iloc[:10, :], barmode='stack', orientation='h', color_discrete_sequence=['#FF9DA6', '#72B7B2'])
    fig_bar.update_layout(
    legend=dict(
        x=0.5,
        y=-0.1,
        xanchor='center',
        yanchor='top',
        orientation='h',
        font=dict(
            family='Arial',
            size=10,
            color='black')))
    fig_bar.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, plot_bgcolor='#eeeeee', paper_bgcolor="#eeeeee")
    return fig_bar

