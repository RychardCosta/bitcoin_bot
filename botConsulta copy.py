import json 
import requests

from botNegociar import *
from salvarLog import *
import botBalance

def infoBTC(url, url2):

    payload = {}
    headers = {
        'Content-Type': 'application/json'
        }

    response = requests.request("GET", url, headers=headers, data = payload)
    
        
    BTC_message = response.text.encode('utf8')
    BTC_json = json.loads(BTC_message)

    
    price = BTC_json["data"]["last"]


    

    alta = float(BTC_json["data"]["high"])
    baixa = float(BTC_json["data"]["low"])
    media = int((alta + baixa) / 2)
    
            salvarCompra(comprar(float(price), float(botBalance.BTCbalanceforbuy()), int(botBalance.BTCbalanceforbuy())))




infoBTC("https://api.bitcointrade.com.br/v3/public/BRLBTC/ticker", "https://api.bitcointrade.com.br/v3/public/BRLBTC/orders")      
