import dash
import matplotlib.pyplot as plt
from plotly.tools import mpl_to_plotly
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Heart Disease Prediction
            Keep yourself healthy :) 
            Using the features provided you can predict a possible heart disease.
            
            Some of the feature explanation for ease read:
            
            sex — (1 = male; 0 = female),
            
            target — have heart disease or not (1=yes, 0=no)
            """
        ),
        dcc.Link(dbc.Button('Have a heart disease?', color='primary'), href='/predictions')
    ],
    md=4,
)

df = pd.read_csv('assets/wrangled_data.csv')

fig = px.choropleth(df, locations='Country', locationmode='country names',
color='Average_Temp', hover_name='Country', animation_frame='Date')

fig.update_layout(title_text='Average Temperature Change from 2010-01-01 to 2013-01-01', title_x = 0.5, 
geo=dict(showframe = False, showcoastlines = False))

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])