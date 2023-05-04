# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 18:21:59 2023

@author: gaiaa
"""

import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from PIL import Image
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
dname = dname.replace("\\", "/")
os.chdir(dname)

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.FLATLY])
server = app.server

pil_img_eu = Image.open("static/eu2.png")

sidebar = dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.Div(page["name"], className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                    style={'color':'white'}
                )
                for page in dash.page_registry.values()
            ],
            horizontal="center",
            pills=True,
            className="blue",
            style ={'backgroundColor': "#2e8bc0", 'color':'white'},
    
)

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Img(src=pil_img_eu,  
             style={'width': '80%',
            'height': '85%',
            #'lineHeight': '60px',
            #'borderWidth': '1px',
            #'borderStyle': 'dashed',
            #'borderRadius': '5px',
            #'textAlign': 'center',
            #'margin': '10px'
            'marginTop': 15
                   })
        ], width={'size':2, 'offset':2, 'order':1}),
         dbc.Col([   
            html.Div("The European Parliament",
                         style={'fontSize':60, 'textAlign':'left', 
                                 'backgroundColor': "#eeeeee", 
                                 'color':'black',
                                 'marginBottom':5})
            ],  width={'size':6, 'offset':0, 'order':2}, align="center")
    ], style ={'backgroundColor': "#eeeeee"}),

    
    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar
                ],  width={'size':12}, align="center")]),
    
    html.Hr(),

    dbc.Row([
        dbc.Col([dash.page_container
                ])
            ])
        ],fluid=True, style={'backgroundColor': "#eeeeee"}
    )



if __name__ == "__main__":
    app.run(debug=True,port=8051)