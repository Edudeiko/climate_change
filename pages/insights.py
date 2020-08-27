# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## **Insights**

            ##### Import libraries first
            ```
            import numpy as np
            import pandas as pd
            import plotly as py
            import plotly.express as px
            import plotly.graph_objs as go
            from plotly.subplots import make_subplots
            from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
            ```
            ##### load the data
            you can download the original data from [here](http://google.com)
            ```
            df = pd.read_csv('../assets/GlobalLandTemperaturesByCountry.csv')
            ```
            ##### Look at the data, find the Null values, clean the data
            ```
            print(df.shape)
            df.head()
            df.tail()
            df.isnull().sum()
            df = df.drop('AverageTemperatureUncertainty', axis=1)
            df = df.rename(columns={'dt': 'Date', 'AverageTemperature': 'Average_Temp'})
            df.isnull().sum()
            df = df.dropna()
            print(df.shape)
            df.head()
            ```
            ##### Creating Celsius to Farenheit function
            ```
            def convert_to_farenheit (c):
                return (c*9/5)+32
            ```
            ##### Round up the result to 2 decimals as well
            ```
            df['Average_Temp_Farenheit'] = df['Average_Temp_Celsius'].apply(convert_to_farenheit).round(2)
            df['Average_Temp_Celsius'] = df['Average_Temp_Celsius'].round(2)
            ```
            ##### Group the dataframe by Country name and dataset
            ```
            df_sorted = df.groupby(['Country', 'Date']).sum().reset_index().sort_values(['Date'], ascending=False)
            df_sorted.head()
            ```
            ##### Create the data range
            ```
            start_date = '2009-12-01'
            end_date = '2013-01-01'
            mask = (df_sorted['Date'] > start_date) & (df_sorted['Date'] <= end_date)
            ```
            ##### Create a new sorted dataset
            ```
            df_2000 = df_sorted[mask]
            print(df_2000.shape)
            df_2000.head()
            ```

            ##### Create a dataset for Climate change by timeline

            ```
            df_2000_by_month = df_2000.groupby(['Date','Country']).sum().reset_index()
            df_2000_by_month.head()
            ```
            ##### Visualization
            ```
            fig = px.choropleth(df_2000_by_month, locations='Country', locationmode='country names', 
                                color='Average_Temp_Farenheit', hover_data=['Average_Temp_Celsius'],
                                hover_name='Country', animation_frame='Date')

            fig.update_layout(title_text='Average Temperature Change from 2010-01-01 to 2013-01-01', title_x = 0.5, 
                              geo=dict(showframe = False, showcoastlines = False))
            fig.show()
            ```
            You can find the GitHub page with all the code by pressing the GitHub icon below.

            """
        ),

    ],
)

layout = dbc.Row([column1])