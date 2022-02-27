import dash
import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, html
from newsapi import NewsApiClient
import outline


outline.app.layout = outline.generateLayout()
print("This ran again")

if __name__ == "__main__":
    outline.app.run_server(debug=True)
