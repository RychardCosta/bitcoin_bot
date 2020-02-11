import json 
import requests

from botNegociar import *
from salvarLog import *

def infoBTC():
    rq = requests.get("https://api.bitcointrade.com.br/v3/public/BRLBTC/ticker")
    BTC_message = rq.text
    
    BTC_json = json.loads(BTC_message)
    #price = BTC_json["data"]["last"]
    price = 44000

    alta = float(BTC_json["data"]["high"])
    baixa = float(BTC_json["data"]["low"])
    media = int((alta + baixa) / 2)

    print(price)

    


        
    if float(price) < float(carregarCompra()) and float(price) <= float(media):
        salvarCompra(comprar(price))
        print("#################" * 7)
    if float(price) > float(carregarCompra()) and float(price) >= float(carregarVenda()) and float(price) >= float(media):
        salvarVenda(vender(price))
        print("#################" * 7) 
            




