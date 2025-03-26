def dividir(numerador,denominador):
    if denominador == 0:
        raise ValueError("Divisão por zero não é permitida!")
    return numerador / denominador
try:
    resultado = dividir(10,0)
    print("Resultado: ",resultado)
except ValueError as erro:
    #captura a exceção e exibe mensagem de erro
    print("Ocorreu um erro", erro)
