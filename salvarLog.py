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
        #print("Nenhuma compra realizada anteriormente!")
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
        #print("Nenhuma Venda realizada anteriormente!")
    except Exception as error:
        print("Erro ao carregar!")
        print(error)



