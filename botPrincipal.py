import time


from botConsulta import infoBTC
import salvarLog

def menu():
    print("######## MENU ########")
    print("1. Ativar bot")
    print("2. Fazer simulação")
    print("3. Relatório de vendas")
    print("4. Relátório de compras")
    print("0. Sair")
    print("######################")

 

url = "https://api.bitcointrade.com.br/v3/public/BRLBTC/ticker"
url2 = "https://api.bitcointrade.com.br/v3/public/BRLBTC/orders"



if __name__ == "__main__":
    while True:

        menu()
        opcao = input("escolha uma opção: ")


        if opcao == '1':
            while True:
                try:
                    infoBTC(url, url2)
                    time.sleep(2)
                except:
                    print("Erro ao ativar o bot!")
                    break
        
        elif opcao == '2':
            pass
       
        elif opcao == '3':
            print('1. Quantidade de vendas:')
            print('2. Valor da ultima venda')
            print('0. voltar')
            opcao2 = input("Qual opção deseja escolher: ")
            if opcao2 == '1':
                if salvarLog.carregarQuantidadeDeVendas():
                    print("Quantidade de vendas realizadas: ", salvarLog.carregarQuantidadeDeVendas())
                else:
                    print("Nenhuma Venda realizada")
                    break
            elif opcao2 == '2':
                if salvarLog.carregarVenda():
                    print("Valor da ultima venda: ", salvarLog.carregarVenda())
                else:
                    print("Nenhuma Venda realizada")
                    break
                            
            elif opcao2 == '0':
                break
            else:
                print('Opção invalida')
            
                

                  

        
        elif opcao == '4':
            while True:
                print('1. Quantidade de compras:')
                print('2. Valor da ultima compra')
                print('0. voltar')
                opcao2 = input("Qual opção deseja escolher: ")
                if opcao2 == '1':
                    if salvarLog.carregarQuantidadeDeCompras():
                        print("Quantidade de compras realizadas: ", salvarLog.carregarQuantidadeDeCompras())
                    else:
                        print("Nenhuma compra realizada")
                        break
                elif opcao2 == '2':
                    if salvarLog.carregarCompra():
                        print("Valor da ultima compra: ", salvarLog.carregarCompra())
                    else:
                        print('Opção invalida')
                        break
                                                
                elif opcao2 == '0':
                    break
                else:
                    print('Opção invalida')


    
        elif opcao == '0':
            print("##### Saindo #####")
            break
        
        else:
            print('Opção invalida') 
        
      
       
