from botConsulta import valorBtcEmTempoReal
from salvarLog import carregarCompra, salvarCompra


if __name__ == "__main__":
    if not carregarCompra():
        valorInicial = input("Digite o valor da sua primeira compra: ")
        salvarCompra(valorInicial)
    
    valorBtcEmTempoReal()
    
    