import requests
import base64

COUNTRY = 'us'
def get_latest_news():
    news_data = requests.get(f'https://newsapi.org/v2/top-headlines?country={COUNTRY}&apiKey=77e164585ab1422893fc26ae68be9f05').json()
    return news_data['articles']

def get_trending_tweets():
    consumer_key = 'Bv0NNWS49eocjcOhbXbxzviuJ'
    consumer_secret_key = 'IsFWTt1JrtRGBe5vlUG6wIRfAze13iJA5CA5bMHYJscOboNFEx'

    # Reformat the keys and encode them
    key_secret = '{}:{}'.format(consumer_key, consumer_secret_key).encode('ascii')
    # Transform from bytes to bytes that can be printed
    b64_encoded_key = base64.b64encode(key_secret)
    # Transform from bytes back into Unicode
    b64_encoded_key = b64_encoded_key.decode('ascii')

    base_url = 'https://api.twitter.com/'
    auth_url = '{}oauth2/token'.format(base_url)
    auth_headers = {
        'Authorization': 'Basic {}'.format(b64_encoded_key),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }
    auth_data = {
        'grant_type': 'client_credentials'
    }
    auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
    #print(auth_resp.status_code)
    access_token = auth_resp.json()['access_token']
    #print(access_token)

    trend_headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }
    trend_params = {
        'id': 1,
    }

    tweets = requests.get(
        "https://api.twitter.com/1.1/trends/place.json", headers=trend_headers, params=trend_params).json()
    #print(tweets[0])
    return tweets[0]['trends']