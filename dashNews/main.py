import outline
import dash_bootstrap_components as dbc
from dash import dcc, Input, Output, html, State

outline.app.layout =  html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(dbc.Input(id="searchField", placeholder="News topics", size="md", className="mb-3"),
                            width="auto"),
                    dbc.Col(dbc.Button("Go!", id="searchButton", className="me-2", n_clicks=0), width="auto"),
                    dbc.Col(dcc.Dropdown(outline.items, id="country", placeholder="CountryDrop"), width=3),
                ]
                , justify="end"),
            dbc.Row([html.H1("Top News Articles", id="title")]),
            dbc.Row(
                [
                    outline.newsCards,
                    outline.tweetList,
                ],
                id="main_row",
            ),
        ]
    )

@outline.app.callback(
        [Output('accordion', 'children'), Output('tweetList', 'children'), Output('title', 'children')],
        Input('searchButton', 'n_clicks'),
        State("searchField", "value"),
        State("country", "value")
    )

def updatePage(n_clicks, searchVal, countryVal):
    new_title, tweets_title = outline.setVars(countryVal, searchVal)
    top = outline.top
    news_articles = []
    for index, article in enumerate(top['articles']):
        news_articles.append(dbc.AccordionItem(
            outline.generateCard(0),
            title=top['articles'][index]['title'],
            item_id="item-{}".format(index),
        ))

    outline.setVars(countryVal, searchVal)
    tweets = outline.tweets
    hold_tweet_list = [dbc.ListGroupItem([
        html.Div(
            [
                html.H5(tweets_title, className="mb-1"),
            ],
            className="d-flex w-100 justify-content-between",
        ),
    ])]

    for i in range(10):
        hold_tweet_list.append(dbc.ListGroupItem(tweets[i]['name'], href=tweets[0]['url']))

    return news_articles, hold_tweet_list, new_title



if __name__ == "__main__":
    outline.app.run_server(debug=False)