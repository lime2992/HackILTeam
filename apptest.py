from flask import Flask, render_template
import tweepy
import yweather
import json

app = Flask(__name__)

#GET trends/available
#trend by location https://developer.twitter.com/en/docs/twitter-api/v1/trends/trends-for-location/api-reference/get-trends-place

#yweather gets the WOEID

auth = tweepy.OAuth2AppHandler(
    'Bv0NNWS49eocjcOhbXbxzviuJ', "IsFWTt1JrtRGBe5vlUG6wIRfAze13iJA5CA5bMHYJscOboNFEx"
)

api = tweepy.API(auth)

#get a country from the drop down list of countries
def create_trend_JSON():
    wc = yweather.Client()
    woeid = wc.fetch_lid("USA")

    #get_place_trends returns a JSON
    JSON_data = api.get_place_trends(woeid, exclude = '#')        

    #We need to put this json data into a file   
    with open("trends.json", "w") as trends:
        json.dump(JSON_data, trends)

    print("Json Created")

@app.route('/')

def index():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)