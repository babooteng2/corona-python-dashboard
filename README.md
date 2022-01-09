# RONACORONA-DASHBOARD

Learning PYTHON GRAPH by building a COVID-19 map

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

# eg

```html
https://dash.plotly.com/layout
https://plotly.com/python-api-reference/generated/plotly.express.scatter_geo.html
https://plotly.com/python/plotly-express/
```
