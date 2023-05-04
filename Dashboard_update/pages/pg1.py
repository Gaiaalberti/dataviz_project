# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 18:23:06 2023

@author: gaiaa
"""

import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
from PIL import Image


dash.register_page(__name__, path='/', name='Home') # '/' is home page

# page 1 data
df = pd.read_csv("dataset/merged_coalition.csv")


#Using Pillow to read the the image
#pil_img = Image.open("C:/Users/gaiaa/OneDrive/Desktop/dash/assets/Rplot.png")
pil_img2 = Image.open("assets/Rplot05.png")
network = Image.open("assets/Graph.png")

card_main = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("Number of MEPs", className="card-title", style={'textAlign':'center','font-size':"20px"}),
                html.Hr(style={'color':'#2e8bc0', 'font-weight': 'bold'}),
                html.H1(
                    "705",
                    className="card-text", style={'textAlign':'center'}
                )
            ]
        ),
    ],
     color="#eeeeee", outline=False # https://bootswatch.com/default/ for more card colors
    #inverse=True,   # change color of text (black or white)
    #outline=True  # True = remove the block colors from the background and header
)

card_second = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("% of female MEPs", className="card-title", style={'textAlign':'center','font-size':"15px"}),
                html.Hr(style={'color':'#2e8bc0', 'font-weight': 'bold'}),
                html.H1(
                    "39%",
                    className="card-text", style={'textAlign':'center'}
                )
            ]
        ),
    ],
     color="#eeeeee", outline=False # https://bootswatch.com/default/ for more card colors
    #inverse=True,   # change color of text (black or white)
    #outline=True  # True = remove the block colors from the background and header
)

card_third = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("% of male MEPs", className="card-title", style={'textAlign':'center', 'font-size':"15px"}),
                html.Hr(style={'color':'#2e8bc0', 'font-weight': 'bold'}),
                html.H1(
                    "61%",
                    className="card-text", style={'textAlign':'center'}
                )
            ]
        ),
    ],
     color="#eeeeee", outline=False # https://bootswatch.com/default/ for more card colors
    #inverse=True,   # change color of text (black or white)
    #outline=True  # True = remove the block colors from the background and header
)


layout = dbc.Container([
    dbc.Row([
        html.Div(children="The European Parliament is the only directly elected institution of the European Union. Thus, it is important that its compostition is representative of the entire european society."),
        html.Div(style={'height':'5px'}), 
        html.Div(children="In this project, we will explore how the European Parliament evolved in terms of political orientation and, more specifically, we will analyze the gender gap that has been characterizing its composition. The European Parliament has made some progress in increasing the representation of women over the terms, but it is still way behind in reaching gender equality. Through data visualization, we will examine the changes in the political parties' representation and if and how this has impacted the gender balance in the European Parliament. This project aims to provide insights into the evolving nature of the European Parliament and the challenges that it faces in achieving gender equality with a final focus on the italian EU representatives."),
        html.Div(style={'height':'20px'}),        
        html.H4("The European Parliament composition today (term 2019-2024)", style={ 'font-weight': 'bold'}),
        html.H6("An overview of the characteristics of the European Parliament today"), #style={ 'font-weight': 'bold'}
        html.Div(style={'height':'40px'}),
        ]),
    dbc.Row([
        dbc.Col([
#            html.Div(children='''The current European Parliament composition per political position.''', 
#                     style={
#            'textAlign': 'center'}),
            html.Img(src=pil_img2,  
             style={'width': '100%',
            'height': '100%',
            #'lineHeight': '60px',
            #'borderWidth': '1px',
            #'borderStyle': 'dashed',
            #'borderRadius': '5px',
            #'textAlign': 'center',
            #'margin': '10px',
            #'marginBottom': 50, 'marginTop': 25
                   })
        ], width={'size':6, 'offset':0, 'order':1}),
       
        dbc.Col([
            dbc.Row([
                dbc.Col(card_main, width={'size':6, 'order':1}, align="center")]), 
            dbc.Row([
                dbc.Col(card_second, width={'size':6, 'order':1}),
                html.Div(style={'height':'20px'}),
                dbc.Col(card_third, width={'size':6, 'order':2})
                ])
                ], width={'size':5, 'offset':1, 'order':2},  align="center")
        ]),
   
    html.Div(style={'height':'50px'}),
        
  
] , style={'backgroundColor': "#eeeeee"})




