import outline
import dash_bootstrap_components as dbc
from dash import dcc, Input, Output, html, State


navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A('NewsFlow', style={'color': 'white', 'fontSize': 45, 'font-weight': 'bold', 'marginRight': 150,
                                      'padding-right': 60}),


            dbc.Col(dbc.Input(id="searchField", placeholder="News topics", size="md", className="mb-3",
                              style={'width': 500, 'height': 40, 'marginTop': 20, 'marginRight': 20}), width="auto"),
            dbc.Col(dcc.Dropdown(outline.items, id="country", placeholder="CountryDrop", style={'height': 40,
                                                                                                'marginRight': 20,
                                                                                                'marginTop': 4}),
                    width=3),
            dbc.Col(dbc.Button("Go!", id="searchButton", className="me-2", n_clicks=0, style={'width': 100,
                                                                                              'height': 40})),

        ]
    ),
    color="dark",
    dark=True,
)

outline.app.layout =  html.Div(
        [
            navbar,

            #dbc.Row(
             #   [
              #      dbc.Col(dbc.Input(id="searchField", placeholder="News topics", size="md", className="mb-3"),
               #             width="auto"),
                #    dbc.Col(dbc.Button("Go!", id="searchButton", className="me-2", n_clicks=0), width="auto"),
                 #   dbc.Col(dcc.Dropdown(outline.items, id="country", placeholder="CountryDrop"), width=3),
                #]
                #, justify="end"),


            dbc.Row([html.H1("Top News Articles")], style={'marginLeft': 10, 'marginBottom': 10, 'marginTop': 25,
                                                           'font-weight': 1000}),
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