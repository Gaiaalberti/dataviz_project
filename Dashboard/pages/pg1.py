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
df = pd.read_csv("merged_coalition.csv")

layout = dbc.Container([
    dbc.Row([
        ])
])

