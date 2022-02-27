import dash
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Container import Container
from dash import Dash, Input, Output, State, html
from newsapi import NewsApiClient
import outline

# API CALL



#SOURCES START

navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.Col(html.Div('Project Title', style={'color': 'white', 'fontSize': 30, 'bold': True})),
            dbc.Col(dbc.Input(placeholder="News topics", size="md", className="mb-3", style={'width': 500, 'height': 40})),
            dbc.Col(dbc.DropdownMenu(label="Country", children=outline.items, className="mb-3"),width="auto"),
            dbc.Col(dbc.Button("Go!", color="primary", className="ms-2", n_clicks=0),width="auto"),
        ]
    ),
    color="dark",
    dark=True,
)


outline.app.layout = html.Div(
    [
        navbar,

        #dbc.Row(
         #   [
          #      dbc.Col(dbc.Input(placeholder="News topics", size="md", className="mb-3"),width="auto"),
           #     dbc.Col(dbc.Button("Go!", id="example-button", className="me-2", n_clicks=0),width="auto"),
            #    dbc.Col(dbc.DropdownMenu(label="Country", children=outline.items, className="mb-3"),width="auto"),
            #]
        #,justify="end"),
        dbc.Row([html.H1("Top News Articles")], style={'marginBottom': 10, 'marginTop': 25}),
        dbc.Row(
            [
                outline.newsCards,
                outline.tweetList,
            ],
        )
    ]
)

if __name__ == "__main__":
    outline.app.run_server()
