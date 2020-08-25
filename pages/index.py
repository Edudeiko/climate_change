import dash
import matplotlib.pyplot as plt
from plotly.tools import mpl_to_plotly
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

import plotly.graph_objs as go
from plotly.subplots import make_subplots
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Climate Change Visualization
            
            For informational purpose
            
            By pointing at any country and by sliding over the years
            you can see how the temperature changes.
            
            
            """
        ),
        dcc.Link(dbc.Button('How I made it?', color='primary'), href='/process')
    ],
    md=3,
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
