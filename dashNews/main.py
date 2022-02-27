import dash
import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, html
from newsapi import NewsApiClient
import outline

# API CALL



#SOURCES START


outline.app.layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(dbc.Input(placeholder="News topics", size="md", className="mb-3"),width="auto"),
                dbc.Col(dbc.Button("Go!", id="example-button", className="me-2", n_clicks=0),width="auto"),
                dbc.Col(dbc.DropdownMenu(label="Country", children=outline.items, className="mb-3"),width="auto"),
            ]
        ,justify="end"),
        dbc.Row([html.H1("Top News Articles")]),
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
