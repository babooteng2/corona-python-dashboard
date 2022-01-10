from dash import html


def make_table(df):
    return html.Table(
        children=[
            html.Thead(
                style={"display": "block", "marginBottom": 25},
                children=[
                    html.Tr(
                        children=[
                            html.Th(column_name.replace("_", " "))
                            for column_name in df.columns
                        ],
                        style={
                            "display": "grid",
                            "gridTemplateColumns": "repeat(4, 1fr)",
                            "fontWeight": "600",
                            "fontSize": "16",
                        },
                    )
                ],
            ),
            html.Tbody(
                children=[
                    html.Tr(
                        children=[
                            html.Td(value_column) for value_column in value
                        ],
                        style={
                            "display": "grid",
                            "gridTemplateColumns": "repeat(4, 1fr)",
                            "border-top": "1px solid white",
                            "padding": "30px 0px",
                            "textAlign": "right",
                        },
                    )
                    for value in df.values
                ],
            ),
        ]
    )
