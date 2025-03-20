import re

texto = "O meu nome é rafael dantas (123) 456-7890"
padrao = r'\(\d{3}\) \d{3}-\d{4}'
#para encontrar numeros de telefone

resultado = re.search(padrao, texto)

if resultado:
    numero_tel = resultado.group()
    print("Numero de telefone encntrado: ",numero_tel)
else:
    print("Numero de telefone não encontrado")
