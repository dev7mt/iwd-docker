from typing import Any, Dict, List, Tuple

import dash_bootstrap_components as dbc
import flask
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import psycopg2
from dash import Dash, Input, Output, dash_table, dcc, html

# creating appliaction
server = flask.Flask(__name__)
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], server=server)

CONN = psycopg2.connect(
    host="mypostgres", database="sales", user="iwd", password="iwd@2022"
)


def check_for_data() -> str:
    cursor = CONN.cursor()
    cursor.execute("select count(*) from clicks")
    data = cursor.fetchall()
    return str(data)


app.layout = html.Div(
    children=[
        html.Span(children="This will be text", id="output_text"),
        dcc.Interval(id="check_interval", interval=1000),
    ]
)


@app.callback(Output("output_text", "children"), Input("check_interval", "n_intervals"))
def check_callback(_) -> str:
    return check_for_data()


if __name__ == "__main__":
    print("Running app!")
    app.run_server(
        port=8062,
        debug=True,
        dev_tools_hot_reload=True,
        dev_tools_hot_reload_max_retry=5,
        dev_tools_hot_reload_interval=5,
    )
