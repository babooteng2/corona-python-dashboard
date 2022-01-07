import dash
from dash import dcc
from dash import html
import plotly.express as px

app = dash.Dash(__name__)

if __name__ == "__main__":
    app.run_server(debug=True)
