import dash
import dash_bootstrap_components as dbc
from newsapi import NewsApiClient
from dash import Dash, Input, Output, html

from dashNews.tweets import get_trending_tweets

tweets = get_trending_tweets()

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

news_articles = []
for index, article in enumerate(top['articles']):
    news_articles.append(dbc.AccordionItem(
                    generateCard(0),
                    title=top['articles'][index]['title'],
                    item_id="item-{}".format(index),
                ))

newsCards = dbc.Accordion(
            news_articles,
            id="accordion",
            active_item="item-1",
            flush=True,
            style={'width':"80%",}
        )



tweetList = dbc.ListGroup(
    [
        dbc.ListGroupItem([
            html.Div(
                [
                    html.H5("Trending Tweets", className="mb-1"),
                ],
                className="d-flex w-100 justify-content-between",
            ),
        ]),
        dbc.ListGroupItem(tweets[0]['name'], href=tweets[0]['url']),
        dbc.ListGroupItem(tweets[1]['name'], href=tweets[1]['url']),
        dbc.ListGroupItem(tweets[2]['name'], href=tweets[2]['url']),
        dbc.ListGroupItem(tweets[3]['name'], href=tweets[3]['url']),
        dbc.ListGroupItem(tweets[4]['name'], href=tweets[4]['url']),
        dbc.ListGroupItem(tweets[5]['name'], href=tweets[5]['url']),
        dbc.ListGroupItem(tweets[6]['name'], href=tweets[6]['url']),
        dbc.ListGroupItem(tweets[7]['name'], href=tweets[7]['url']),
        dbc.ListGroupItem(tweets[8]['name'], href=tweets[8]['url']),
        dbc.ListGroupItem(tweets[9]['name'], href=tweets[9]['url']),
        dbc.ListGroupItem(tweets[10]['name'], href=tweets[10]['url']),
    ],
    style={"width":"20%"}
)


