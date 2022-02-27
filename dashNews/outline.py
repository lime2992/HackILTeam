import dash
import dash_bootstrap_components as dbc
from newsapi import NewsApiClient
from dash import Dash, Input, Output, html, State, dcc

#from dashNews.tweets import get_trending_tweets

#tweets = get_trending_tweets()

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)



api = NewsApiClient(api_key='c3714ae8334b4794b63ffc101502f54a')
top = api.get_top_headlines()

items = [
    "First","Second","Third"
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
                dbc.AccordionItem(
                    generateCard(5),
                    title=top['articles'][5]['title'],
                    item_id="item-6",
                ),
                dbc.AccordionItem(
                    generateCard(6),
                    title=top['articles'][6]['title'],
                    item_id="item-7",
                ),
                dbc.AccordionItem(
                    generateCard(7),
                    title=top['articles'][7]['title'],
                    item_id="item-8",
                ),
                dbc.AccordionItem(
                    generateCard(8),
                    title=top['articles'][8]['title'],
                    item_id="item-9",
                ),
                dbc.AccordionItem(
                    generateCard(9),
                    title=top['articles'][9]['title'],
                    item_id="item-10",
                ),
                dbc.AccordionItem(
                    generateCard(10),
                    title=top['articles'][10]['title'],
                    item_id="item-11",
                ),
            ],
            id="accordion",
            active_item="item-1",
            flush=True,
            style={'width':"80%",}
        )



#tweetList = dbc.ListGroup(
#    [
#        dbc.ListGroupItem([
#            html.Div(
#                [
#                    html.H5("Trending Tweets", className="mb-1"),
#                ],
#                className="d-flex w-100 justify-content-between",
#            ),
#        ]),
#        dbc.ListGroupItem(tweets[0]['name'], href=tweets[0]['url']),
#        dbc.ListGroupItem(tweets[1]['name'], href=tweets[1]['url']),
#        dbc.ListGroupItem(tweets[2]['name'], href=tweets[2]['url']),
#        dbc.ListGroupItem(tweets[3]['name'], href=tweets[3]['url']),
#       dbc.ListGroupItem(tweets[4]['name'], href=tweets[4]['url']),
#       dbc.ListGroupItem(tweets[5]['name'], href=tweets[5]['url']),
#       dbc.ListGroupItem(tweets[6]['name'], href=tweets[6]['url']),
#       dbc.ListGroupItem(tweets[7]['name'], href=tweets[7]['url']),
#      dbc.ListGroupItem(tweets[8]['name'], href=tweets[8]['url']),
#       dbc.ListGroupItem(tweets[9]['name'], href=tweets[9]['url']),
#       dbc.ListGroupItem(tweets[10]['name'], href=tweets[10]['url']),
#
#   ],
#   style={"width":"20%"}
#

def generateLayout():
	print("generate layout ran again")
	app.layout = html.Div(
	    [
		dbc.Row(
		    [
		        dbc.Col(dbc.Input(id="searchField",placeholder="News topics", size="md", className="mb-3"),width="auto"),
		        dbc.Col(dbc.Button("Go!", id="searchButton", className="me-2", n_clicks=0),width="auto"),
		        dbc.Col(dcc.Dropdown(items,id="country",placeholder="CountryDrop"),width=3),
		    ]
		,justify="end"),
		dbc.Row([html.H1("Top News Articles")]),
		dbc.Row(
		    [
		        newsCards,
		        #tweetList,
		    ],
		), html.Div(id="useless"),
	    ]
	)
	
	return app.layout
	
@app.callback(
    Output("useless","children"),
    Input("searchButton","n_clicks"),	
    State("searchField", "value"),
    State("country", "value"),
)
def newSearch(n_clicks,searchVal,value):
	if(n_clicks != 0):
		app.layout = generateLayout()
		
