import time


from botConsulta import infoBTC



if __name__ == "__main__":
    while True:
        try:
            infoBTC()
            time.sleep(2)
        except Exception as error:
            print("Erro ao executrar o programa!")
            break
        
      
       
