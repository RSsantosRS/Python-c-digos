def divide(x,y):
    try:
        resultado = x / y
    except ZeroDivisionError:
        print("opa, para ai! Voce não pode fazer essa divisão!!")
    else:
        print("Certa! A sua resposta está certa!",resultado)
    finally:
        #este bloco SEMPRE executa
        # Independende de erros
        print("Isso sempre acontece")

divide(3,0)
divide(3,2)
divide(3,0)
