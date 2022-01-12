# Corona-Python-Dashboard

Learning PYTHON GRAPH by building a COVID-19 map

https://corona-python-dashboard.herokuapp.com/

```node
https://coronavirus.jhu.edu/map.html

download csv file for death, confirm, recover data from
https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data
```

## INSTALLATION

```node
pip install pandas
pip install dash
pip install jupyterlab
pip install jupyterthemes

pip install black
pip install pylint

// for deploy
pip install gunicorn
```

```node
Extension: Excel viewer
right click -> open with
select open with CSV viewer
or
open file and ctrl + shift + p
select or type CSV:Open Preview

// jupyter theme change
 jt -t monokai
```

### check linting and formatting when you use Python

```node
// in vscode -> ctrl + shift + p -> open workspace setting(JSON)
{
  "python.pythonPath": "",
  "python.formatting.provider": "black",
  "python.formatting.blackArgs": ["--line-length", "80"],
  "editor.formatOnSave": true,
  "python.linting.pylintEnabled": true,
  "python.linting.enabled": true,
  "python.linting.lintOnSave": true,
  "python.linting.pylintArgs": ["--load-plugins", "pylint-flask"],
  "[python]": {
    "editor.defaultFormatter": "ms-python.python"
  }
}
```

default formatter prettier가 되어있는 설정을 python사용 시에는 python formatter 이용 선언

# ref.

```html
https://dash.plotly.com/layout
https://plotly.com/python-api-reference/generated/plotly.express.scatter_geo.html
https://plotly.com/python/plotly-express/
https://plotly.com/python/builtin-colorscales/#using-builtin-continuous-color-scales
https://plotly.com/python/reference/layout/xaxis/
https://dash.plotly.com/dash-core-components/input
https://plotly.com/python/line-charts/ https://plotly.com/python/time-series/
https://dash.plotly.com/react-for-python-developers
https://dash.plotly.com/dash-core-components
```

### deploy on heroku

```node
curl https://cli-assets.heroku.com/install.sh | sh
heroku login
heroku git:remote -a [프로젝트명]
git push heroku master

https://devcenter.heroku.com/articles/procfile
```
