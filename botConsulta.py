import json 
import ssl

import websocket
import requests

from botNegociar import *
from salvarLog import *


def on_message(ws, message):
    message = json.loads(message)
    price = message["data"]["price"]
    media = 10000

    
    print("###################3")
    print("Preço atual do BTC: ", price)
    print("Ultima Compra: ", carregarCompra())
    if carregarVenda():
        print("Ultima venda: ", carregarVenda())
    else:
        pass
    print("###################")
    
    
    if price <= float(carregarCompra()) and price <= float(media):
        salvarCompra(comprar(price))
        print("#################")
    if price > float(carregarCompra()) and price >= float(carregarVenda()):
        salvarVenda(vender(price))
        print("#################")

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    print("### Abrindo conexao ###")

    jsonSubscribe = """
{
    
        "event": "bts:subscribe",
        "data": { 
            "channel": "live_trades_btcusd"
        }
} 
"""
    ws.send(jsonSubscribe)

def valorBtcEmTempoReal():
    ws = websocket.WebSocketApp("wss://ws.bitstamp.net.",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)

    ws.on_open = on_open
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})