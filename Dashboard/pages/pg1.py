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
import networkx as nx
import plotly.express as px


dash.register_page(__name__, path='/', name='Home') # '/' is home page

# page 1 data
df = pd.read_csv("dataset/merged_coalition.csv")

#Using Pillow to read the the image
#pil_img = Image.open("C:/Users/gaiaa/OneDrive/Desktop/dash/assets/Rplot.png")
pil_img2 = Image.open("assets/Rplot05.png")

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




network = Image.open("assets/Graph.png")

#needed for last graph
term7 = df[df["term"]== "2009-2014"]
term8 = df[df["term"]== "2014-2019"]
term9 = df[df["term"]== "2019-2024"]
merged789 = pd.concat([term7, term8, term9])
dati7 = {'source': 'term7', 'target': [*term7['fullName'].tolist()]}
df1 = pd.DataFrame(dati7, columns=['source','target'])
dati8 = {'source': 'term8', 'target': [*term8['fullName'].tolist()]}
df2 = pd.DataFrame(dati8, columns=['source','target'])
dati9 = {'source': 'term9', 'target': [*term9['fullName'].tolist()]}
df3 = pd.DataFrame(dati9, columns=['source','target'])
result = pd.concat([df1, df2, df3])
g = nx.from_pandas_edgelist(result, source='source', target='target')
# create a dataset with all deputies that have been elected for all three terms
three_terms = pd.DataFrame(columns = merged789.columns)
for node in g:
    if sum(result[result['target'] == node].value_counts()) == 3:
        three_terms = pd.concat([three_terms, merged789[merged789['fullName'] == node]], ignore_index=True)





layout = dbc.Container([
    dbc.Row([
        html.H4("The European Parliament composition today (term 2019-2024)", style={'textAlign': 'center', "color" : "black", 'font-weight': 'bold'}),
        html.Div(children="The European Parliament (formerly European Parliamentary Assembly or Common Assembly) is the parliament of the European Union (EU) and together with the Council of Ministers, it is the law-making branch of the institutions of the Union. It meets in two locations: Strasbourg and Brussels."),
        html.Div(children="The European Parliament is the only directly elected institution of the European Union, and its composition has changed significantly over the years. MEPs are the elected representatives of EU citizens; they represent their interests and those of their cities or regions in Europe. They listen to people with local and national concerns, interest groups and businesses. Thus, it is important that the compostition of the parliament is representative of the European society."),
        html.Div(children="Our aim is to investigate this composition, paying particular attention to gender gap."),
        html.Div(children="Let's start by giving an overview of the characteristics of the European Parliament today."),
        html.Div(style={'height':'40px'})
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
   dbc.Row(
       dbc.Col([
           
           
           ])),
   html.Div(style={'height':'20px'}),
   
    dbc.Row(
        dbc.Col([
            html.Div(children="In this project, we will explore how the European Parliament evolved in terms of political orientation and, more specifically, we will analyze the gender gap that has been characterizing its composition. The European Parliament has made some progress in increasing the representation of women over the terms, but it is still way behind in reaching gender equality. Through data visualization, we will examine the changes in the political parties' representation and if and how this has impacted the gender balance in the European Parliament. This project aims to provide insights into the evolving nature of the European Parliament and the challenges that it faces in achieving gender equality.", 
                     )
])),html.Div(style={'height':'50px'}),
    
     dbc.Row([
         
         dbc.Col([
             html.H4('Network of deputies in the last three terms (2009-current)', 
                     style={'textAlign': 'center', "color" : "black", 'font-weight': 'bold'}),
             html.Div(children="The network below helps us to understand if, starting from term 7 (2009-2014), some MEPs have been re-elected for the subsequent terms. We can notice that term 7 and 8 (hence the ones going from 2009 until 2019) have shared a lot of deputies, some of which have also stayed for one more term, and are currently elected. Moreover, a small group of deputies has participated to term 7 and again to term 9, skipping a term."), 
             html.Div(children="Remark: Only the last three terms have been taken into consideration, to get an understanding of the recent trends."),
             html.Div(children="We have considered interesting to see whether some MEPs have changed political orientation between one term and another."
            )], width=12)]),    
    
     html.Div(style={'height':'20px'}),
     
    
    
      dbc.Row([
          
          dbc.Col([
              html.Img(src=network,  
               style={'width': '100%',
              'height': '100%',
                     })
          ], width={'size':7, 'offset':0, 'order':1}),
          
        
          dbc.Col([
              
              dbc.Row([
                  
                      html.H4(children = 'Changes in political orientation of reelected deputies', 
                                          style={'textAlign': 'center', "color" : "black", 'font-weight': 'bold'},
                                          className=' mb-4')            
                      
                      ]), 
              html.Div(style={'height':'20px'}),
              
              
              dbc.Row([
                      dcc.Dropdown(id='drdw', multi=False, value='2009-2014',
                                   options=[{'label':x, 'value':x} for x in three_terms['term'].unique()])
                                   ]), 
             
              html.Div(style={'height':'20px'}),
             
                
              dbc.Row([
                      dcc.Graph(id = "anim_bar")
                  ]),
              
              html.Div(style={'height':'60px'}),

              ] ,width={'size':5, 'offset':0,'order':2}),
          
          
          ]), html.Div(style={'height':'100px'}),     


], style={'backgroundColor': "#eeeeee"})


@callback(
    Output("anim_bar", "figure"), 
    Input("drdw", "value"))




# Define a function to create the bar chart for a given term
def create_bar_chart(term):
    # Define the desired order of political orientations
    orientation_order = ['left', 'centre-left', 'centre', 'centre-right', 'right', 'Non aligned']
    # Define the colors to use for each political orientation
    colors = {'left': 'red', 'centre-left': 'orange', 'centre': 'yellow', 'centre-right': 'green', 'right': 'blue', 'Non aligned': 'gray'}
    # Filter the dataframe for the selected term
    filtered_df = three_terms[three_terms['term'] == term]
    # Group by political orientation and count the number of deputies in each group
    counts = filtered_df.groupby('orientation')['fullName'].count().reset_index(name='count')
    # Reorder the counts by the desired order of political orientations
    counts = counts.set_index('orientation').reindex(orientation_order).reset_index()
    # Create the bar chart using Plotly
    fig = px.bar(counts, x='orientation', y='count', color='orientation', color_discrete_map=colors, text='count')
    fig.update_layout(title='Deputies in term {}'.format(term))
    fig.update_layout(plot_bgcolor='#eeeeee', paper_bgcolor="#eeeeee")
    
    return fig



# # Define a function to create the bar chart for a given term
# def create_bar_chart(term):

#     # Define the colors to use for each political orientation
#     colors = {'left': 'red', 'centre-left': 'orange', 'centre': 'yellow', 'centre-right': 'green', 'right': 'blue', 'Non aligned': 'gray'}
#     # Filter the dataframe for the selected term
#     filtered_df = three_terms[three_terms['term'] == term]
#     # Group by political orientation and count the number of deputies in each group
#     counts = filtered_df.groupby('orientation')['fullName'].count().reset_index(name='count')
#     # Create the bar chart using Plotly
#     fig = px.bar(counts, x='orientation', y='count', color='orientation', color_discrete_map=colors)
    
#     fig.update_layout(title='Deputies in term {}'.format(term))
#     fig.update_layout(plot_bgcolor='#eeeeee', paper_bgcolor="#eeeeee")

#     return fig

