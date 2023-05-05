# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 18:21:59 2023

@author: gaiaa
"""

#importing needed libraries 
import dash
from dash import html
import dash_bootstrap_components as dbc
from PIL import Image
import os

#setting the path to call datasets and images 
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
dname = dname.replace("\\", "/")
os.chdir(dname)

#defining the app
app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.FLATLY])

#define the variable for heroku platform
server = app.server

#Using Pillow to read the image
pil_img_eu = Image.open("static/eu2.png")

#creating and styling the navigation bar 
navbar = dbc.Nav([
            dbc.NavLink([
                html.Div(page["name"], className="ms-2")],
                href=page["path"],
                active="exact",
                style={'color':'white'})
                for page in dash.page_registry.values()],
            horizontal="center",
            pills=True,
            className="blue",
            style ={'backgroundColor': "#2e8bc0", 'color':'white'})

#formatting the layout of all the pages 
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            # inserting the image 
            html.Img(src=pil_img_eu,  
             style={'width': '80%',
            'height': '85%',
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


    dbc.Row([
        dbc.Col([
            navbar #inserting the navbar previously created
                ],  width={'size':12}, align="center")]),
    
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dash.page_container #calling the content of the pag1/pag2/pag3 
                ])
            ])
        ],fluid=True, style={'backgroundColor': "#eeeeee"}
    )

#executing the app
if __name__ == "__main__":
    app.run(debug=True,port=8051)