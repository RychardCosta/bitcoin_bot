import requests
import json

import api_key

def simular():
    url = "https://api.bitcointrade.com.br/v3/market/estimated_price?amount=583.23&pair=BRLBTC&type=buy"
    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': api_key.api_key,
    }   

    response = requests.request("GET", url, headers=headers, data = payload)
    responseJson = json.loads(response.text.encode('utf8'))

    print(responseJson)


simular()