import requests
import json

import api_key

def BTCbalance():
    url = "https://api.bitcointrade.com.br/v3/wallets/balance"
    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': api_key.api_key,
    }   

    response = requests.request("GET", url, headers=headers, data = payload)
    responseJson = json.loads(response.text.encode('utf8'))

    return responseJson
