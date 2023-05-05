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
import numpy as np

dash.register_page(__name__, name='Gender Gap')

# page 2 data
df = pd.read_csv("dataset/merged_coalition.csv")

def bar_line():
    grouped = df.groupby(["term"])["gender"].value_counts(normalize=True).unstack()
    grouped = grouped.reset_index()
    fig2 = px.line(x=grouped["term"], y=((grouped["female"])*100).round(2),#color=px.Constant("Trend"),
             labels=dict(x="Term", y="% of females MEPs")) #color="Legend"
    fig2.update_traces(line_color='black', line_width=2)
    fig2.add_bar(x=grouped["term"], y=(grouped["female"])*100, name="% of female MEPs",
            marker_color='#FF92A5')
    fig2.update_layout(plot_bgcolor='#eeeeee', paper_bgcolor="#eeeeee")
    return fig2


layout=dbc.Container([

    dbc.Row([
        dbc.Col([
            html.H4(children = 'Gender Gap in the European Parliament thoruoghout the terms (1979-2024)', 
                    style={'textAlign': 'left', "color" : "black", 'font-weight': 'bold'}),
            html.H6("Over the years, there has been a growing awareness of the gender gap and the need to address it in various fields, including politics. Political parties and organizations have made commitments to increase the representation of women in decision-making positions as we can see from the upward trend of the graph below."
            )], width=12)]),  
    
    dbc.Row([
        dbc.Col([dcc.Graph(figure=bar_line())],
                width={'size':8
                       , 'offset':0,
                       'order':1}),
        dbc.Col([
            html.H6(" Interestingly, between the seventh (2009-2014) and eighth term (2014-2019), there was not a significant increase in the percentage of women as one might expect, especially given the increased focus and discussion on gender equality in the last decade. Even if, there has been a progress  we are still far from achieving gender parity. This highlights the need for continued efforts to increase the representation of women in politics and address the persistent gender gap.",
                   style={'textAlign': 'center', "color" :"black"})],
            width={'size':4,'offset': 0 , "order":2 }
        )], align= "center"
),
    html.Div(style={'height':'30px'}),

    dbc.Row([
        dbc.Col([
            html.H4(children = 'Female MEPs representation from each country and by orientation thoruoghout the terms (1979-2024)', 
                    style={'textAlign': 'left', "color" : "black", 'font-weight': 'bold'}),
            html.H6("Change the term and see how the percentage of women in the European Parliament changes across countries and through the different political orientations."
            )], width=12)]),


    html.Div(style={'height':'20px'}),
    
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(id='dpdn', multi=False, value='2019-2024',
                         options=[{'label':x, 'value':x} for x in df['term'].unique()])], width={'size':4, 'offset': 4 })
                         ]), 
    
    html.Div(style={'height':'50px'}),
    
    dbc.Row([
        dbc.Col([        
            dcc.Graph(id = "map"),
            html.Div(style={'height':'70px'}),
            html.H6(children = "From the map, we can observe how the Nordic countries like Finland and Sweden have more women deputities (57%) than male deputies, while, Eastern countries have lower women representatives. It is interesting to notice how Germany, one of the pillar countries of the EU, has a lower percentage of female MEPS than the other western european countries. ",
                    style={'textAlign': 'justify'}),
        ],width={'size':5, 'offset':0,'order':1}),

        dbc.Col([
            dcc.Graph(id = "bar"),
            html.Div(style={'height':'20px'}),
            html.H6(children = "From the bar chart, we can notice how for the center and left political orientation the percentage of women is almost always higher than the percentage of women for the right political orientation. Overall, the gender gap decreases steadily over time for all orientation.",
                    style={'textAlign': 'justify'}),
        ],width={'size':5, 'offset':2,'order':2}),
        
    ]),
    

    html.Div(style={'height':'60px'}), 


    dbc.Row([
        dbc.Col([
            html.H4('The progess in gender equality in each country', 
                    style={'textAlign': 'left', "color" : "black", 'font-weight': 'bold'}),
            html.H6("The visualization below allows us understand whether there has been a costant upward positive trend for gender parity in each country or whether there are has been a decrease in women representation during specific periods"
           )], width=12)]),    
    
    html.Div(style={'height':'20px'}),
    
     dbc.Row([
         dbc.Col([
            dcc.Dropdown(id='drp_country', multi=False, value='Germany',
                         options=[{'label':x, 'value':x} for x in np.sort(df['country'].unique())])]
            , width={'size':5})]),  

    dbc.Row([
         dbc.Col([            
            dcc.Graph(id="bar_line1", )
            
        ], width=7),
        
        dbc.Col([
            html.H6(children="As previously stated, Germany is not charactrerized by a very high female representation contrary on what one would expect since it had a female Chancellor for 16 years until 2021. By looking at the numbers for each term, we notice how the % of women does not increase steadily as years go by. Actually, almost no improvements has been made in reducing the gender gap in the last decade.", 
                     style={'textAlign': 'center'}),
            html.Div(style={'height':'20px'}),
            html.H6(children="Check the trend of other countries to discover their progress in gender equality!", 
                     style={'textAlign': 'center', 'font-weight': 'bold', 'font-style': 'italic' })], width={'size':5}, align = "center"       
        )],className=' mb-4')
   
])


@callback(
    Output('map','figure'),
    Input('dpdn', 'value'))

def update_graph(dpdn):
    dff = df[df['term'] == dpdn]
    grouped = dff.groupby(["country"])["gender"].value_counts(normalize=True).unstack().reset_index()
    fig = px.choropleth(grouped, locations = "country", locationmode="country names", color="female" , scope= "europe", hover_name="country", color_continuous_scale = "RdPu", range_color=[0,1])
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, height=400, # increase the height of the chart
                  width=655, coloraxis_colorbar=dict(
        xanchor='left',
        len=0.8,
        yanchor='middle',
        y=0.5,
        thickness=13,
        tickfont=dict(size=13)))
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
            size=13,
            color='black')))
    fig_bar.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, plot_bgcolor='#eeeeee', paper_bgcolor="#eeeeee", )
    return fig_bar

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
    return fig_1
