import dash
from dash import dcc
from dash import html
import plotly.express as px
from data import countries_df

print(countries_df.values)

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
            style={"textAlign": "center", "paddingTop": "50px"},
            children=[html.H1("Corona Dashboard", style={"fontSize": 50})],
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Table(
                            children=[
                                html.Thead(
                                    children=[
                                        html.Tr(
                                            children=[
                                                html.Th(
                                                    column_name.replace(
                                                        "_", " "
                                                    )
                                                )
                                                for column_name in countries_df.columns
                                            ]
                                        )
                                    ]
                                ),
                                html.Tbody(
                                    children=[
                                        html.Tr(
                                            children=[
                                                html.Td(value_column)
                                                for value_column in value
                                            ]
                                        )
                                        for value in countries_df.values
                                    ]
                                ),
                            ]
                        )
                    ]
                )
            ]
        ),
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)
