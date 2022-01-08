import dash
from dash import dcc
from dash import html
import plotly.express as px
from data import countries_df
from builders import make_table

stylesheets = [
    "https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css",
    "https://fonts.googleapis.com/css2?family=Open+Sans&family=Source+Sans+Pro:wght@300;400&display=swap",
]

app = dash.Dash(__name__, external_stylesheets=stylesheets)

app.layout = html.Div(
    style={
        "minHeight": "100vh",
        "backgroundColor": "#111111",
        "color": "white",
        "fontFamily": "Open Sans, sans-serif",
    },
    children=[
        html.Header(
            style={
                "textAlign": "center",
                "paddingTop": "50px",
                "marginBottom": 100,
            },
            children=[html.H1("Corona Dashboard", style={"fontSize": 50})],
        ),
        html.Div(children=[html.Div(children=[make_table(countries_df)])]),
    ],
)

map_figure = px.scatter_geo(countries_df)
map_figure.show()

if __name__ == "__main__":
    app.run_server(debug=True)
