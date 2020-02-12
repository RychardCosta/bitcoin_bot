import salvarLog
import requests
import json

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

    print("Compra realizada no valor de: R$ ", float(valor))
    salvarLog.salvarQuantidadeDeCompras(salvarLog.carregarQuantidadeDeCompras())

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
    print("Venda realizada no valor de: R$ ", float(valor))
    salvarLog.salvarQuantidadeDeVendas(salvarLog.carregarQuantidadeDeVendas())
    return valor



