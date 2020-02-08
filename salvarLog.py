import pickle


def salvarCompra(ultimaCompra):
    try:
        with open("database.db", "wb") as file:
            pickle.dump(ultimaCompra, file)

    except Exception as error:
        print("Erro ao salvar!")
        print(error)

def carregarCompra():
    try:
        with open("database.db", "rb") as file:
            ultimaCompra = pickle.load(file)
        
            return ultimaCompra

    except FileNotFoundError: 
        print("Nenhuma compra realizada anteriormente!")
    except Exception as error:
        print("Erro ao carregar!")
        print(error)
