import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
from data import (
    countries_df,
    totals_df,
    dropdown_options,
    make_global_df,
    make_country_df,
)
from builders import make_table

stylesheets = [
    "https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css",
    "https://fonts.googleapis.com/css2?family=Open+Sans&family=Source+Sans+Pro:wght@300;400&display=swap",
]

app = dash.Dash(__name__, external_stylesheets=stylesheets)

server = app.server

bubble_map = px.scatter_geo(
    countries_df,
    title="Confirmed By Country",
    size="Confirmed",
    size_max=40,
    hover_name="Country_Region",
    color="Confirmed",
    locations="Country_Region",
    locationmode="country names",
    projection="natural earth",
    template="plotly_dark",
    color_continuous_scale=px.colors.sequential.Oryel,
    hover_data={
        "Confirmed": ":,",
        "Deaths": ":,",
        "Recovered": ":,",
        "Country_Region": False,
    },
)
bubble_map.update_layout(
    margin=dict(l=0, r=0, t=50, b=0),
    coloraxis_colorbar=dict(xanchor="left", x=0),
)

bars_graph = px.bar(
    totals_df,
    x="condition",
    y="count",
    template="plotly_dark",
    title="Total Global Cases",
    hover_data={"condition": False, "count": ":,"},
    labels={"condition": "Condition", "count": "Count", "color": "Condition"},
)

bars_graph.update_traces(marker_color=["#e74c3c", "#8e44ad", "#27ae60"])

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
        html.Div(
            style={
                "display": "grid",
                "gap": 40,
                "gridTemplateColumns": "repeat(4, 1fr)",
                "padding": 20,
            },
            children=[
                html.Div(
                    style={"gridColumn": "span 3"},
                    children=[dcc.Graph(figure=bubble_map)],
                ),
                html.Div(children=[make_table(countries_df)]),
            ],
        ),
        html.Div(
            children=[
                html.Div(
                    style={
                        "display": "grid",
                        "gap": 40,
                        "gridTemplateColumns": "repeat(4, 1fr)",
                        "padding": 20,
                    },
                    children=[
                        html.Div(dcc.Graph(figure=bars_graph)),
                        html.Div(
                            style={
                                "gridColumn": "span 3",
                            },
                            children=[
                                dcc.Dropdown(
                                    style={
                                        "width": 320,
                                        "margin": "0 auto",
                                        "color": "#111111",
                                    },
                                    placeholder="Select a Country",
                                    id="country",
                                    options=[
                                        {"label": country, "value": country}
                                        for country in dropdown_options
                                    ],
                                ),
                                dcc.Graph(id="country_graph"),
                            ],
                        ),
                    ],
                ),
            ]
        ),
    ],
)


@app.callback(Output("country_graph", "figure"), [Input("country", "value")])
def update_hello(value):
    if value is None:
        df = make_global_df()
    else:
        df = make_country_df(value)
    fig = px.line(
        df,
        x="date",
        y=["confirmed", "deaths", "recovered"],
        template="plotly_dark",
        labels={
            "value": "Cases",
            "variable": "Conditions",
        },
        hover_data={
            "value": ":,",
            "variable": False,
        },
        color_discrete_map={
            "confirmed": "#e74c3c",
            "deaths": "#8e44ad",
            "recovered": "#27ae60",
        },
    )
    fig.update_xaxes(
        rangeslider_visible=True,
    )
    return fig
