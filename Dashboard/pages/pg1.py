# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 18:23:06 2023

@author: gaiaa
"""

#importing the libraries 
import dash
from dash import html
import dash_bootstrap_components as dbc
import pandas as pd
from PIL import Image
import os

#setting the path to call datasets and images 
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
dname = dname.replace("\\", "/")
os.chdir(dname)

#Creating page Home and linking to the 
dash.register_page(__name__, path='/', name='Home') 

# importing the dataframe 
df = pd.read_csv(dname + "/dataset/merged_coalition.csv")

#saving the parliament chart made in r and exported in png in a variable
pil_img2 = Image.open("static/Rplot.png")

#Creating the first card to put information about the current EU parliament
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
     color="#eeeeee", outline=False 
)

#creating the second card to put information about the current EU parliament
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
     color="#eeeeee", outline=False
)

#creating the second card to put information about the current EU parliament
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
     color="#eeeeee", outline=False 
)

#creating the content for the first page 
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
            html.Img(src=pil_img2,  
             style={'width': '100%',
            'height': '100%',
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
   
    html.Div(style={'height':'40px'}),
    
    dbc.Row([
        dbc.Col([
            html.H4(children="Find out our findings in the next sections!", 
                     style={'textAlign': 'center', 'font-weight': 'bold'})], width={'size':12})
        ])
  
] , style={'backgroundColor': "#eeeeee"})









