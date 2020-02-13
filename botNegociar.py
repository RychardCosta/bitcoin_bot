import salvarLog
import requests
import json

import botBalance
import api_key

def comprar(valor, quanti):
    
    url = "https://api.bitcointrade.com.br/v3/market/create_order"
    payload = "{\n  \"pair\":\"BRLBTC\",\n  \"amount\": " + str(float(quanti)) + ",\n  \"type\": \"sell\",\n  \"subtype\": \"limited\",\n  \"unit_price\": " + str(int(valor)) + "\n""}"
    payload2 = "{\n  \"pair\":\"BRLBTC\",\n  \"amount\": 0.5,\n  \"type\": \"sell\",\n  \"subtype\": \"limited\",\n  \"unit_price\": 14500\n}"

    headers = {
        'Content-Type': 'application/json',
        'x-api-key': api_key.api_key,
    }   

    response = requests.request("POST", url, headers=headers, data = payload)
    responseJson = json.loads(response.text.encode('utf8'))

    message = responseJson["message"]

    print(message)

    salvarLog.salvarQuantidadeDeCompras(salvarLog.carregarQuantidadeDeCompras(), botBalance.BTCbalanceforbuy())

    return valor

def vender(valor, quanti):
    url = "https://api.bitcointrade.com.br/v3/market/create_order"
    payload = "{\n  \"pair\":\"BRLBTC\",\n  \"amount\": " + str(float(quanti)) + ",\n  \"type\": \"sell\",\n  \"subtype\": \"limited\",\n  \"unit_price\": " + str(int(valor)) + "\n""}"
    payload2 = "{\n  \"pair\":\"BRLBTC\",\n  \"amount\": 0.5,\n  \"type\": \"buy\",\n  \"subtype\": \"limited\",\n  \"unit_price\": 14500\n}"

    headers = {
        'Content-Type': 'application/json',
        'x-api-key': api_key.api_key,
    }   

    response = requests.request("POST", url, headers=headers, data = payload)
    responseJson = json.loads(response.text.encode('utf8'))

    message = responseJson["message"]

    print(message)

    salvarLog.salvarQuantidadeDeVendas(salvarLog.carregarQuantidadeDeVendas(), botBalance.BTCbalanceforsell())
    return valor



