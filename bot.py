import json 


import websocket
import requests

def on_message(ws, message):
    message = json.loads(message)

    price = message["data"]["price"]
    
    print("Valor do BTC em tempo real: $", price)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    print("### opened ###")

    jsonSubscribe = """
{
    
        "event": "bts:subscribe",
        "data": { 
            "channel": "live_trades_btcusd"
        }
} 
"""
    ws.send(jsonSubscribe)

if __name__ == "__main__":
    rq = requests.get("https://api.bitcointrade.com.br/v3/public/BRLBTC/ticker")
    ws = websocket.WebSocketApp("wss://ws.bitstamp.net/",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)

    ws.on_open = on_open
    ws.run_forever()
