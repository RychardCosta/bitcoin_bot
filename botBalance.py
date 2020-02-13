import requests
import json

import api_key

def BTCbalanceforbuy():
    url = "https://api.bitcointrade.com.br/v3/wallets/balance"
    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': api_key.api_key,
    }   

    response = requests.request("GET", url, headers=headers, data = payload)
    responseJson = json.loads(response.text.encode('utf8'))

    valorDisponivel = responseJson["data"][0]["available_amount"]

    return float(valorDisponivel)

def BTCbalanceforsell():
    url = "https://api.bitcointrade.com.br/v3/wallets/balance"
    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': api_key.api_key,
    }   

    response = requests.request("GET", url, headers=headers, data = payload)
    responseJson = json.loads(response.text.encode('utf8'))

    valorDisponivel = responseJson["data"][1]["available_amount"]


    return float(valorDisponivel)

