import dash
import dash_core_components as dcc
import dash_html_components as html
# import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import dash_table
import pandas as pd
from datetime import datetime as dt
import time
import os
import random

import numpy as np

app = dash.Dash(__name__, external_stylesheets=[])

app.layout = html.Div([

    # Dataset dropdown
    html.Div([
        html.H2(children="הרצאה בלעדית במחנט 2020:", id="Opening",
                style={
                    "direction": "rtl"
                }),
        html.H1(children="איך להיות צוות שיווק טוב", id="Text",
                style={
                    "direction": "rtl"
                }),
        html.Button("תן לי את זה יא מניאאאאקקקק", id="button", n_clicks=0,
                    style={
                        "horizontalAlign": "Middle",
                        "display": "inline"
                    }),
    ], style={
        "textAlign": "center",
        "marginTop": "33vh"
    })
], style={"width": "100vw"})


# Functions

def generateRandom():
    data = pd.read_csv(r"Data\data.csv")

    while True:
        rand_template_index = random.randrange(0, len(data["template"]))
        rand_template = data["template"][rand_template_index]
        if pd.isna(rand_template):
            continue
        break
    print(rand_template)
    print(rand_template_index)
    random_line = ""
    for letter in rand_template:
        if letter == "@":
            objects = pd.Series(data["object"])
            objects = objects.str.split(",", expand=True)
            objects = pd.concat([objects[0], objects[1].dropna(), objects[2].dropna()])
            rand_object_index = random.randrange(0, len(objects))
            rand_object = objects.iloc[rand_object_index]
            letter = rand_object
        random_line = random_line + letter

    return random_line


# CALLBACKS

@app.callback(Output("Text", "children"),
              [Input("button", "n_clicks")])
def text_callback(n_clicks):
    if n_clicks > 0:
        return generateRandom()
    else:
        return "איך להיות צוות שיווק טוב"


if __name__ == "__main__":
    app.run_server()
