import pickle


def salvarCompra(ultimaCompra):
    try:
        with open("databaseCompra.db", "wb") as file:
            pickle.dump(ultimaCompra, file)

    except Exception as error:
        print("Erro ao salvar!")
        print(error)

def carregarCompra():
    try:
        with open("databaseCompra.db", "rb") as file:
            ultimaCompra = pickle.load(file)
        
            return ultimaCompra

    except FileNotFoundError: 
        pass

    except Exception as error:
        print("Erro ao carregar!")
        print(error)




def salvarVenda(ultimaVenda):
    try:
        with open("databaseVenda.db", "wb") as file:
            pickle.dump(ultimaVenda, file)

    except Exception as error:
        print("Erro ao salvar!")
        print(error)

def carregarVenda():
    try:
        with open("databaseVenda.db", "rb") as file:
            ultimaVenda = pickle.load(file)
        
            return ultimaVenda

    except FileNotFoundError: 
        pass
 
    except Exception as error:
        print("Erro ao carregar!")
        print(error)




def salvarQuantidadeDeCompras(Compra=0):
    try:
        Compra = Compra + 1
        
        with open("quantidadeDeCompras.db", "wb") as file:
            pickle.dump(Compra, file)

    except Exception as error:
        print("Erro ao salvar!")
        print(error)

def carregarQuantidadeDeCompras():
    try:
        with open("quantidadeDeCompras.db", "rb") as file:
            quantidadeDeCompras = pickle.load(file)
        
            return quantidadeDeCompras

    except FileNotFoundError: 
        pass
       
    except Exception as error:
        print("Erro ao carregar!")
        print(error)


def salvarQuantidadeDeVendas(Venda=0):
    try:
       Venda = Venda + 1
       with open("quantidadeDeVendas.db", "wb") as file:
            pickle.dump(Venda, file)

    except Exception as error:
        print("Erro ao salvar!")
        print(error)

def carregarQuantidadeDeVendas():
    try:
        with open("quantidadeDeVendas.db", "rb") as file:
            carregarQuantidadeDeCompras = pickle.load(file)
        
            return carregarQuantidadeDeVendas

    except FileNotFoundError: 
        pass
        
    except Exception as error:
        print("Erro ao carregar!")
        print(error)