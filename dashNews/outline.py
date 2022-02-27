import dash
import dash_bootstrap_components as dbc
from newsapi import NewsApiClient
from dash import dcc, Input, Output, html, State

from dashNews.tweets import get_trending_tweets, get_countries

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

countries = get_countries()
alpha_countries = []
for country in countries:
    alpha_countries.append(country)

alpha_countries.sort()

items = []
for location in alpha_countries:
    items.append(location)
items.pop()

api = NewsApiClient(api_key='77e164585ab1422893fc26ae68be9f05')

top = api.get_top_headlines()
tweets = get_trending_tweets(1)

def setVars(location, query):
    global tweets
    global top
    top = api.get_top_headlines()
    tweets = get_trending_tweets(1)
    if location is None:
        tweets = get_trending_tweets(1)
    else:
        print(countries)
        tweets = get_trending_tweets(countries[location]["twitterid"])
        print(tweets)

    if query is not None and location is not None:
        print(countries[location]["newsid"])
        top = api.get_top_headlines(country=countries[location]["newsid"], q=query)

    if query is None and location is not None:
        print(countries[location]["newsid"])
        top = api.get_top_headlines(country=countries[location]["newsid"])

    if query is not None and location is None:
        top = api.get_top_headlines(q=query)

    print(top)

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
    style={'width': "80%", }
)

hold_tweet_list = []
hold_tweet_list.append(dbc.ListGroupItem([
            html.Div(
                [
                    html.H5("Trending Tweets", className="mb-1"),
                ],
                className="d-flex w-100 justify-content-between",
            ),
        ]),)

for i in range(10):
    hold_tweet_list.append(dbc.ListGroupItem(tweets[i]['name'], href=tweets[0]['url']))

tweetList = dbc.ListGroup(
    hold_tweet_list,
    style={"width": "20%"},
    id="tweetList",
)