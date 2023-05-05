# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 18:23:25 2023

@author: gaiaa
"""
#importing the libraries
import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np

#Creating page Italy and linking to the main app
dash.register_page(__name__, name='Italy')

# importing the dataframe Italy (subset of the merged_coalition dataset)
df = pd.read_csv("dataset/merged_coalition.csv")
df_italy = pd.read_csv("dataset/italy.csv")

#creating the content for the third page 
layout=dbc.Container([

#First paragraph    
    html.Div(style={'height':'20px'}),
    dbc.Row([
        html.H4(children="Italian female MEPs in the European Parliament", 
                style={'textAlign': 'left', "color" : "black", 'font-weight': 'bold'}),
        html.H6(children="Let's look at the progress made by Italy in increasing the percentage of italian female deputies in the EU with a comparison with other European countries."),
        html.Div(style={'height':'15px'}), 
        ]),
    
    dbc.Row([
        dbc.Col([
            #creating the dropdown in which to select the country
            dcc.Dropdown(id='dpdn_italy', multi=True, value=['Italy', "Germany"],
                         options=[{'label':x, 'value':x} for x in np.sort(df['country'].unique())]
                         )
                ], width={'size':4})
        ]),     
    
    dbc.Row([
        dbc.Col([dcc.Graph(id="line_italy")], # define the line plot
                width={'size':8
                       , 'offset':0,
                       'order':1}),
        dbc.Col([
            #commenting the line plot
            html.H6("In recent years, Italy has experienced a remarkable surge in the proportion of female MEPs, particularly since 2004, culminating in nearly achieving gender parity in 2019. Notably, during the earlier terms of the parliament, a significant disparity in gender parity existed between Germany, which exhibited a relatively high percentage of female representation for that period, and Italy. Nevertheless, in the last two terms, this situation has been completely reversed.",
                   style={'textAlign': 'center', "color" :"black"}),
            html.Div(style={'height':'20px'}),
            html.H6(children="You can choose other countries to compare their trend in gender equality with the trend of Italy!", 
            style={'textAlign': 'center', 'font-weight': 'bold', 'font-style': 'italic' })
            ],
            width={'size':4,'offset': 0 , "order":2 }
        )], align= "center" ),
 
#Second paragraph
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
            #Creating first dropdown where you chose the specific term
            dcc.Dropdown(id='drop1', multi=False, value='2019-2024',
                         options=[{'label':x, 'value':x} for x in df_italy['term'].unique()])
            ],width={'size':4, 'offset':2}),
        
        dbc.Col([
            #creating the second dropdown where you choose either to investigate about the national group or the european group
            dcc.Dropdown(id='drop2', multi=False, value='nation_group',
                         options=[
        {'label': 'National party', 'value': 'nation_group'},
        {'label': 'European group', 'value': 'eu_group_1'}
    ])
            ],width={'size':4})]),
 
    dbc.Row([
        dbc.Col([      
            #define the bar chart about italy
            dcc.Graph(id="bar_chart_italy")   
        ])
    ])
])


#Callback section

#linking the multi dropdown component to the line plot 
@callback(
    Output('line_italy','figure'),
    Input('dpdn_italy', 'value'))

#creating the function to plot the choropleth map
def line_plot(country):
    dff = df[df['country'].isin(country)]
    grouped_it = dff.groupby(["term", "country"])["gender"].value_counts(normalize=True).unstack()
    grouped = grouped_it.reset_index()
    fig4 = px.line(x=grouped["term"], y=((grouped["female"])*100).round(2),color=grouped['country'],
             labels=dict(x="Term", y="% of females MEPs"))
    #fig4.update_traces(line_color='pink', line_width=4)
    fig4.update_layout(plot_bgcolor='#eeeeee', paper_bgcolor="#eeeeee",  hoverlabel=dict(font=dict(color='white')))
    return fig4



#linking the dropdown component relative to the term to the map 
@callback(
    Output('bar_chart_italy', 'figure'),
    [Input('drop1', 'value'),
     Input('drop2', 'value')])

#linking the dropdown component relative to the terms to the horizontal stacked bar chart
def bar_line(drop1, drop2):
    dff_italy = df_italy[df_italy['term'] == drop1]
    # Group data by selected group
    if drop2 == 'nation_group':
        grouped_df = dff_italy.groupby(['nation_group', 'gender']).size().reset_index(name='count')
        grouped_df = grouped_df.sort_values(by='count', ascending=False)
        fig5 = px.bar(grouped_df, x="nation_group", y='count', color='gender',
                         barmode='stack',
                         color_discrete_map={'male': '#72B7B2', 'female': '#FF92A5'})
        fig5.update_layout(
            height=600,
            xaxis=dict(
                tickmode='array',
                ticktext=grouped_df['nation_group'].apply(lambda x: '<br>'.join(x.split())).tolist(),
                tickvals=grouped_df['nation_group'].tolist()
            ))
    else:
        grouped_df = dff_italy.groupby(['eu_group_1', 'gender']).size().reset_index(name='count')
        grouped_df = grouped_df.sort_values(by='count', ascending=False)
        fig5 = px.bar(grouped_df, x="eu_group_1", y='count', color='gender',
                         barmode='stack',
                         color_discrete_map={'male': '#72B7B2', 'female': '#FF92A5'},
                         )
        fig5.update_layout(
            height=600,
            xaxis=dict(
                tickmode='array',
                ticktext=grouped_df['eu_group_1'].apply(lambda x: '<br>'.join(x.split())).tolist(),
                tickvals=grouped_df['eu_group_1'].tolist()
            ))
    
    fig5.update_xaxes(tickangle=0, 
                            automargin=True, 
                            tickfont=dict(size=10),
                            title=dict(text=drop2, font=dict(size=12)))
    fig5.update_layout(
    xaxis_title="Parties",
    yaxis_title='Number of Deputies',
    plot_bgcolor='#eeeeee', paper_bgcolor="#eeeeee",
    hoverlabel=dict(font=dict(color='white')))
    return fig5
        
    
 