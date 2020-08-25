# Interactive map of Climate change through the years of 2010 to 2013

You can find the project at [here](https://www.dj-helper.com/).

## 2️ Project Overview

Climate change web app is made for anyone interested in having a closer look at an actual proof of the changing climate over the years from 2010 to 2013. The years can be adjusted, original dataset link included.

### Tech Stack

Python, Dash, Plotly, Heroku, Flask

### 2️⃣ Explanatory Variables

- Country
- Date
- Average_Temperature

### Data Sources

- Original dataset can be found here [here](https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data)
- To explore more about Plotly[here](https://plotly.com/python/)

### Python Notebooks

[Notebooks](https://github.com/Edudeiko/climate_change/tree/master/notebooks)

### Setting up the environment

- conda create --name {your app name} python=3.8.5
- pip install pipenv
- pipenv install
- pipenv shell
- install all of the environments needed (dash, dash_bootstrap_components, gunicorn, plotly, pandas)
- Create file requirement text by using 'pip freeze > requirements.txt'
- python run.py
- Then in your browser, go to http://localhost:8050/


## Heroku

- Check the directory first
- Create file requirement text by using 'pip freeze > requirements.txt'
- pipenv shell
- heroku login
- git remote -v
- git push heroku master

## Debug mode

- heroku run bash
- ---> ls -al
- ---> exit
- heroku config
- heroku config:set SPOTIFY_CLIENT_ID="---------------"
- heroku config:set SPOTIFY_CLIENT_SECRET="---------------"
- heroku config # > to check on the changes

## Important

- Add your heroku app name to the spotify app --> dashboard --> redirect URIs


# Dash Template

[Instructions](https://lambdaschool.github.io/ds/unit2/dash-template/)
