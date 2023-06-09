## Gender Gap page

#importing the libraries
import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
from PIL import Image
import os


#setting the path to call datasets and images 
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
dname = dname.replace("\\", "/")
os.chdir(dname)

#Creating page Gender Gap and linking to the main app
dash.register_page(__name__, name='Gender Gap')

# importing the merged and filan dataset
df = pd.read_csv("dataset/merged_coalition.csv")

#importing dataset for network
merged_network = pd.read_csv("dataset/merged_network.csv")

#importing the png of the network created using networkx library
network = Image.open("static/Graph.png")

#creating the function to plot the first bar chart
def bar_line():
    grouped = df.groupby(["term"])["gender"].value_counts(normalize=True).unstack()
    grouped = grouped.reset_index()
    fig = px.line(x=grouped["term"], y=((grouped["female"])*100).round(2),
             labels=dict(x="Term", y="% of females MEPs")) 
    fig.update_traces(line_color='black', line_width=2)
    fig.add_bar(x=grouped["term"], y=(grouped["female"])*100, name="% of female MEPs",
            marker_color='#FF92A5')
    fig.update_layout(plot_bgcolor='#eeeeee', paper_bgcolor="#eeeeee")
    return fig


#creating the content for the second page 
layout=dbc.Container([

#First paragraph
    dbc.Row([
        dbc.Col([

            html.H4(children = 'Gender Gap in the European Parliament thoruoghout the terms (1979-2024)', 
                    style={'textAlign': 'left', "color" : "black", 'font-weight': 'bold'}),
            html.H6("Over the years, there has been a growing awareness of the gender gap and the need to address it in various fields, including politics. Political parties and organizations have made commitments to increase the representation of women in decision-making positions as we can see from the upward trend of the graph below."
            )], width=12)]),  
    
    dbc.Row([
        dbc.Col([dcc.Graph(figure=bar_line())], #inserting the bar line previously defined with the function
                width={'size':8
                       , 'offset':0,
                       'order':1}),
        dbc.Col([
            #commenting the graph
            html.H6(" Interestingly, between the seventh (2009-2014) and eighth term (2014-2019), there was not a significant increase in the percentage of women as one might expect, especially given the increased focus and discussion on gender equality in the last decade. Even if, there has been a progress  we are still far from achieving gender parity. This highlights the need for continued efforts to increase the representation of women in politics and address the persistent gender gap.",
                   style={'textAlign': 'center', "color" :"black"})],
            width={'size':4,'offset': 0 , "order":2 }
        )], align= "center"
),
    html.Div(style={'height':'30px'}), #inserting a space

#Second paragraph
    dbc.Row([
        dbc.Col([
            html.H4(children = 'Female MEPs representation from each country and by orientation thoruoghout the terms (1979-2024)', 
                    style={'textAlign': 'left', "color" : "black", 'font-weight': 'bold'}),
            html.H6("Change the term and see how the percentage of women in the European Parliament changes across countries and through the different political orientations."
            )], width=12)]),


    html.Div(style={'height':'20px'}),
    
    dbc.Row([
        dbc.Col([
            #creating the dropdown in which to choose the term
            dcc.Dropdown(id='dpdn', multi=False, value='2019-2024',
                         options=[{'label':x, 'value':x} for x in df['term'].unique()])], width={'size':4, 'offset': 4 })
                         ]), 
    
    html.Div(style={'height':'50px'}),
    
    dbc.Row([
        dbc.Col([        
            
            #define the map 
            dcc.Graph(id = "map"),
            html.Div(style={'height':'70px'}),
            #commenting the map
            html.H6(children = "From the map, it is evident that the Scandinavian countries like Finland and Sweden have reached gender parity, whereas the representation of women from Eastern countries is much lower. It is interesting to notice how Germany, one of the pillar countries of the EU, has a lower percentage of female MEPS than the other countries of Western Europe.",
                    style={'textAlign': 'justify'}),
        ],width={'size':5, 'offset':0,'order':1}),

        dbc.Col([
            #defining the stacked bar chart
            dcc.Graph(id = "bar"),
            html.Div(style={'height':'20px'}),
            #commenting the insights ftom the bar chart
            html.H6(children = "The bar chart reveals that the proportion of female MEPs in center and left wing parties is almost always greater than the percentange of female MEPs in right wing parties. Overall, the gender gap has decreased steadily over time for all orientations.",
                    style={'textAlign': 'justify'}),
        ],width={'size':5, 'offset':2,'order':2}),
        
    ]),
    

    html.Div(style={'height':'60px'}), 

# Third Paragraph
    dbc.Row([
        dbc.Col([
            html.H4('The progess in gender equality in each country', 
                    style={'textAlign': 'left', "color" : "black", 'font-weight': 'bold'}),
            html.H6("The visualization below allows us understand whether there has been a costant upward positive trend for gender parity in each country or whether there are has been a decrease in women representation during specific periods."
           )], width=12)]),    
    
    html.Div(style={'height':'20px'}),
    
     dbc.Row([
         dbc.Col([
             #creating a new dropdown in which to choose the country
            dcc.Dropdown(id='drp_country', multi=False, value='Germany',
                         options=[{'label':x, 'value':x} for x in np.sort(df['country'].unique())])]
            , width={'size':5})]),  

    dbc.Row([
         dbc.Col([  
            # define the horizontal bar chart 
            dcc.Graph(id="bar_chart", )
            
        ], width=7),
        
        dbc.Col([
            #Commenting the insights from the bar chart 
            html.H6(children="As mentioned earlier, despite being led by a female Chancellor for a period of 16 years until 2021, Germany does not exhibit a significantly high representation of women in the EU parliament, which may come as a surprise. Upon closer examination of the data for each term, it is apparent that the percentage of female MEPs has not increased in a consistent manner over time. In fact, there has been negligible progress made in reducing the gender gap in the last decade.", 
                     style={'textAlign': 'center'}),
            html.Div(style={'height':'20px'}),
            html.H6(children="Check the trend of other countries to discover their progress in gender equality!", 
                     style={'textAlign': 'center', 'font-weight': 'bold', 'font-style': 'italic' })], width={'size':5}, align = "center"       
        )],className=' mb-4'),

    html.Div(style={'height':'20px'}),


# Fourth Paragraph    
    dbc.Row([
        
        dbc.Col([
            html.H4('Network of deputies in the last three terms (2009-current)', 
                    style={'textAlign': 'left', "color" : "black", 'font-weight': 'bold'}),    
            
            html.Div(children="The visualization below represents the network of the European parliament members across three terms starting from term 7 (2009-2014) to term 9 (2019-2024). The aim is to understand how many members have been re-elected for the subsequent terms. The blue points represent the MEPs that have just been elected for that term. The green points represent MEPs that have been re-elected twice while the red dots represent the MEPs that have re-elected for all three terms from 2009 up to now. Then, we analyzed the affiliation of these re-elected members and whether there are big differences in the numbers of re-elected women vs re-elected men ."),
            html.Div(style={'height':'10px'}),            
            html.Div(children="Remark: Only the last three terms have been taken into consideration, to get an understanding of the recent trends.",
                    style={'font-weight': 'bold','font-style': 'italic' } ),

           ], width=12)]),    
   
    html.Div(style={'height':'20px'}),
    
     dbc.Row([       
         dbc.Col([
             #inserting the network 
             html.Img(src=network,  
              style={'width': '100%',
             'height': '100%',
                    })
         ], width={'size':6, 'offset':0, 'order':1}),
        
         dbc.Col([            
             dbc.Row([                
                     html.H5(children = 'Analysis of the gender of the re-elected MEPs in each political orientation.', 
                                         style={'textAlign': 'center', "color" : "black"},
                                         className=' mb-4')            
                     
                     ]), 
             html.Div(style={'height':'20px'}),
             
             
             dbc.Row([
                 #creating the dropdown
                     dcc.Dropdown(id='drdw', multi=False, value='2 terms (7-8)',
                                  options=[
                 {'label': 'MEPs of term 7 re-elected only for term 8', 'value': '2 terms (7-8)'},
                 {'label': 'MEPs of term 8 re-elected only for term 9', 'value': '2 terms (8-9)'},
                 {'label': 'MEPs of term 7 re-elected only for term 9', 'value': '2 terms (7-9)'},
                 {'label': 'MEPs of term 7 re-elected for both term 8 & 9 ', 'value': '3 terms'}
                                  ])]),
            
             html.Div(style={'height':'20px'}),
            
               
             dbc.Row([
                 #defining the bar chart
                     dcc.Graph(id = "anim_bar")
                 ]),
             
             html.Div(style={'height':'60px'}),

             ] ,width={'size':5, 'offset':1,'order':2}),
         
         
         ]), 
     
     html.Div(style={'height':'50px'}),

     dbc.Row([      
         dbc.Col([
             #Commenting the insights from the bar chart 
             html.H6(children=" We can notice that term 7 and 8 (hence the ones going from 2009 until 2019) have shared a lot of deputies, some of which have also been re-elected for the current term (2019-2024). Moreover, a small group of deputies has participated to term 7 and again to term 9, skipping a term. From the bar chart, it is interesting to notice how for the right wing there is always a very small or null percentage of women re-elected in contrast with the centre and left wing where the % percentage of women re-elected is similar to the % percentage of men re-elected for that political orientation",  
                 style={'textAlign': 'center'}),
             ])]
             ,className=' mb-4'),     
   
   
])

#Callback section


#linking the dropdown component relative to the term to the map 
@callback(
    Output('map','figure'),
    Input('dpdn', 'value'))

#creating the function to plot the choropleth map
def create_map(term):
    dff = df[df['term'] == term]
    grouped = dff.groupby(["country"])["gender"].value_counts(normalize=True).unstack().reset_index()
    fig1 = px.choropleth(grouped, locations = "country", locationmode="country names", color="female" , scope= "europe", hover_name="country", color_continuous_scale = "RdPu", range_color=[0,1])
    fig1.update_layout( margin={ "r":0,"t":0,"l":0,"b":0}, height=400, width=655, 
                       #adjusting the position of the legend for the map
                       coloraxis_colorbar=dict(xanchor='left', len=0.8, yanchor='middle', y=0.5, thickness=13,tickfont=dict(size=13)),
                       plot_bgcolor='#eeeeee', paper_bgcolor="#eeeeee")
    return fig1


#linking the dropdown component relative to the terms to the horizontal stacked bar chart
@callback(
    Output('bar','figure'),
    Input('dpdn', 'value'))

#creating the function to plot the stacked bar chart for the different political orientation
def create_bar(term):
    dff = df[df['term'] == term]
    grouped = dff.groupby(['orientation', 'gender']).size().reset_index(name='counts')
    pivoted2 = grouped.pivot(index='orientation', columns='gender', values='counts')
    pivoted2 = pivoted2.reindex(pivoted2.sum(axis=1).sort_values(ascending=False).index)
    pivoted2 = pivoted2.div(pivoted2.sum(axis=1), axis=0)
    pivoted2 = pivoted2.reindex(['left', 'centre-left', 'centre', 'centre-right', 'right', 'Non aligned'])
    fig2 = px.bar(pivoted2, barmode='stack', orientation='h', color_discrete_sequence=['#FF9DA6', '#72B7B2'])
    
    fig2.update_layout(margin={"r":0,"t":0,"l":0,"b":0},
                       legend=dict( x=0.5, y=-0.15, xanchor='center',yanchor='top',orientation='h',
                                  font=dict( size=11, color='black')),
                       xaxis_title="% of male/female MEPs",
                       plot_bgcolor='#eeeeee', paper_bgcolor="#eeeeee", 
                       hoverlabel=dict(font=dict(color='white')
                            )
                       )
    return fig2


#linking the dropdown 2 component relative to countries to the horizontal bar chart 
@callback(
    Output('bar_chart','figure'),
    Input('drp_country', 'value'))

#creating the function to plot the stacked bar chart for % of female representative vs % of male MEPS in the different countries
def create_bar_1(country):
    dff = df[df["country"] == country]
    grouped = dff.groupby(['term', 'gender']).size().reset_index(name='counts')
    pivoted = grouped.pivot(index='term', columns='gender', values='counts')
    pivoted = pivoted.div(pivoted.sum(axis=1), axis=0)
    pivoted = pivoted.reindex(pivoted.sum(axis=1).sort_values(ascending=False).index)
    fig3 = px.bar(pivoted, barmode='stack', orientation='h',color_discrete_map={"female": "#FF92A5", "male": "#72B7B2"})
    fig3.update_layout(xaxis_title="% of male/female MEPs", yaxis_title='term', plot_bgcolor='#eeeeee', paper_bgcolor="#eeeeee", hoverlabel=dict(font=dict(color='white')))
    return fig3


#linking the dropdown 3 component relative to the terms to the stacked bar chart
@callback(
    Output("anim_bar", "figure"), 
    Input("drdw", "value"))

#creating the function to plot the stacked bar chart with plotly where:

def create_bar_chart(mandate):
    filtered_df = merged_network[merged_network['mandate_length'] == mandate]
    grouped = filtered_df.groupby(['orientation', 'gender']).size().reset_index(name='count')
    # Plot the stacked bar chart using Plotly Express
    category_order = ['female', 'male']
    fig6 = px.bar(grouped, x='orientation', y='count', color='gender', barmode='stack',category_orders={'gender': category_order},
                 labels={'orientation': 'Orientation', 'count': 'Count', 'gender': 'Gender'},
    color_discrete_map={"female": "#FF92A5", "male": "#72B7B2"},)
    
    fig6.update_layout(showlegend=True, legend_title_text='Gender',plot_bgcolor='#eeeeee', paper_bgcolor="#eeeeee", hoverlabel=dict(font=dict(color='white')))
    fig6.update_xaxes(categoryorder='array', categoryarray= ['left', 'centre-left', 'centre', 'centre-right', 'right', 'Non aligned'])
    return fig6