import json 
import requests

from botNegociar import *
from salvarLog import *

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
    
    

    print("Valor do BTC: R$ ", float(price))
    print("Valor da média do BTC: R$ ", float(media))

       
    if carregarVenda():
        if not carregarQuantidadeDeVendas():
            print("Nenhuma venda realizada até o momento!")
        else:
            print("Ultima venda: R$ ", float(carregarVenda()))
            print("Quantidade de vendas: ", carregarQuantidadeDeVendas())
    
    if not carregarVenda():
        salvarVenda(media)
    
    if carregarCompra():
        if not carregarQuantidadeDeCompras():
            print("Nenhuma compra realizada até o momento!")
            print("################### " * 7)     
        else:
            print("Ultima compra: R$ ", float(carregarCompra()))
            print("Quantidade de compras: ", carregarQuantidadeDeCompras())
            print("################### " * 7)

    if not carregarCompra():
        salvarCompra((media))  

        
    if float(price) < float(carregarCompra()) and float(price) <= float(media):
        try:
            salvarCompra(comprar(float(price)))
            print("#################" * 7)
        except:
            print("Falha ao realizar a compra!")
            print("#################" * 7)
            
    if float(price) > float(carregarCompra()) and float(price) > float(carregarVenda()):
        try:
            salvarVenda(vender(float(price)))
            print("#################" * 7)
        except:
            print("Falha ao realizar a venda!")
            print("#################" * 7)




            

