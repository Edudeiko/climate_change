# Interactive map of Climate change through the years of 2010 to 2013

You can find deployed to Heroku project [here](https://climate-change-overview.herokuapp.com).

## Project Overview

Climate change web app is made for anyone interested in having a closer look at an actual proof of the changing climate over the years from 2010 to 2013. The years can be adjusted, original dataset link included.

### Tech Stack

Python, Dash, Plotly, Heroku, Flask

### Explanatory Variables

- Country
- Date
- Average_Temperature_Celsius
- Average_Temperature_Farenheit

### Data Sources

- Original dataset can be found here [here](https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data)
- To explore more about Plotly [here](https://plotly.com/python/)

### Python Notebooks

[Notebooks](https://github.com/Edudeiko/climate_change/tree/master/notebooks)

### Setting up the environment

- Check the directory first
- conda create --name {your app name} python=3.8.5
- pip install pipenv
- pipenv install
- pipenv shell
- install all of the environments needed (dash, dash_bootstrap_components, gunicorn, plotly, pandas)
- Create file requirement text by using 'pip freeze > requirements.txt'
- python run.py
- Then in your browser, go to http://localhost:8050/

### Make all the changes needed, than repeat the steps to check on the result

- python run.py
- Then in your browser, go to http://localhost:8050/

## Deploy to Heroku

- pipenv shell
- Test your app locally, with Gunicorn: ``` gunicorn run:server ```
- Go to https://dashboard.heroku.com/new-app and give your app a name.
- heroku login
- heroku git:remote -a your-app-name
- git add .
- git commit -am "ready to deploy to heroku"
- git push heroku master
