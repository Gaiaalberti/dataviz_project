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


dash.register_page(__name__, name='Gender Gap')

df = pd.read_csv("merged_coalition.csv")


layout=dbc.Container([
    dbc.Row([
        
    ])
])
