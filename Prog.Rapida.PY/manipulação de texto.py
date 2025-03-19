class Aula_Hoje:
    def exemplo_01():
        texto = "Meu nome é Rafael Dantas e estou manipulando String"
        print(texto[0:20:2])
        #conta do "0" ate o "20" de "2"em "2" linhas

    def exemplo_02():
        texto = "Meu nome é Rafael Dantas e estou manipulando String"
        print(len(texto))
        #conta a quatidade de caracteres do texto

    def exemplo_03():
        texto = "Meu nome é Rafael Dantas e estou manipulando String"
        print(texto.count("a"))
        #conta quantos "a" existem no texto (somente minusculo nesse caso)
    
    def exemplo_04():
        texto = "Meu nome é Rafael Dantas e estou manipulando String"
        print(texto.count("a",5,30))
        #conta quantos "a" existem do caractere "5" ate o "30" ( somente minusculo nesse caso)

    def exemplo_05():
        texto = "Meu nome é Rafael Dantas e estou manipulando String"
        print(texto.find("Rafael"))
        #procura a palavra e entrega o indice dessa palavra solicitada (uma casa antes dela começar), exibe -1 se não existir


    def exemplo_06():
        texto = "Meu nome é Rafael Dantas e estou manipulando String"
        novo_texto = texto.replace ("manipulando","trabalhando com")
        print(novo_texto)
        #altera o texto expecifico do arquivo pela parte escolhida
    
    def exemplo_07():
        texto = "Meu nome é Rafael Dantas e estou manipulando String"
        print(texto.lower())
        print(texto.upper())
        print(texto.capitalize())
        print(texto.title())
        print(texto.swapcase())
        #realiza diversas formatações no texto
    
    def exemplo_08():
        nome = str(input("Digite seu nome: "))
        print(f"olá, {nome}!")
        print(f"ola,{nome.strip()}!")
        #retira o espaço antes ou depois do texto
        
    def exemplo_09():
        texto = "Nossa aula manipulado string"
        print(' '.join(texto))
        print(texto.split())
        print(' '.join(texto.split()))
        #mostra diversas formas de "cortar" e editar os textos


    if __name__ == "__main__":
        exemplo_09()
