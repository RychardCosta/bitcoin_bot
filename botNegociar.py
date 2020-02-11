import salvarLog

def comprar(valor=0):
    print("Compra realizada no valor de: R$ ", float(valor))
    salvarLog.salvarQuantidadeDeCompras(salvarLog.carregarQuantidadeDeCompras())

    return valor

def vender(valor=0):
    print("Venda realizada no valor de: R$ ", float(valor))
    salvarLog.salvarQuantidadeDeVendas(salvarLog.carregarQuantidadeDeVendas())
    return valor
