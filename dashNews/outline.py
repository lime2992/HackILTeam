import dash
import dash_bootstrap_components as dbc
from newsapi import NewsApiClient
from dash import Dash, Input, Output, html


app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)


api = NewsApiClient(api_key='c3714ae8334b4794b63ffc101502f54a')
top = api.get_top_headlines()

items = [
    dbc.DropdownMenuItem("First"),
    dbc.DropdownMenuItem(divider=True),
    dbc.DropdownMenuItem("Second"),
]

def generateCard(i):
    card = dbc.Card(
        [
            dbc.Row(
                [
                    dbc.Col(
                        dbc.CardImg(
                            src=top['articles'][i]['urlToImage'],
                            className="img-fluid rounded-start",
                        ),
                        className="col-md-4",
                    ),
                    dbc.Col(
                        dbc.CardBody(
                            [
                                html.H4(top['articles'][i]['description'], className="card-text"),
                                dbc.Button(
                                    top['articles'][i]['source']['name'],
                                    href=top['articles'][i]['url'],
                                    target="_blank",
                                    external_link=True,
                                    color="primary",
                                ),
                            ]
                        ),
                        className="col-md-8",
                    ),
                ],
                className="g-0 d-flex align-items-center",
            )
        ],
        className="mb-3",
        style={"maxWidth": "100%"},
    )
    
    return card

newsCards = dbc.Accordion(
            [
                dbc.AccordionItem(
                    generateCard(0),
                    title=top['articles'][0]['title'],
                    item_id="item-1",
                ),
                dbc.AccordionItem(
                    generateCard(1),
                    title=top['articles'][1]['title'],
                    item_id="item-2",
                ),
                    dbc.AccordionItem(
                    generateCard(2),
                    title=top['articles'][2]['title'],
                    item_id="item-3",
                ),
                    dbc.AccordionItem(
                    generateCard(3),
                    title=top['articles'][3]['title'],
                    item_id="item-4",
                ),
                    dbc.AccordionItem(
                    generateCard(4),
                    title=top['articles'][4]['title'],
                    item_id="item-5",
                ),
            ],
            id="accordion",
            active_item="item-1",
            flush=True,
            style={'width':"80%",}
        )
        
tweetList = dbc.ListGroup(
    [
        dbc.ListGroupItem("Item 1"),
        dbc.ListGroupItem("Item 2"),
        dbc.ListGroupItem("Item 3"),
    ],
    style={"width":"20%"}
)


