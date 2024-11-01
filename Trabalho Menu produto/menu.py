from trabalho import Produto

def main_menu():
    produtos = []  #cria uma lista para armazenar varios produtos

    while True: # "enquanto" for true (diferente da opção 5) rodará o sistema permitindo a manipulação da lista
        print("\nMenu de Opções")
        print("1. Adicionar produto")
        print("2. Exibir informações de todos os produtos")
        print("3. Atualizar preço de um produto")
        print("4. Atualizar quantidade de um produto")
        print("5. Sair")

        escolha = input("Escolha uma opção: ") #pede ao usuario que selecione a opção desejada para prosseguir o código

        if escolha == "1":
            nome = input("Digite o nome do produto que deseja cadastrar: ")
            preco = float(input("Digite o preço do produto: "))
            quantidade = int(input("Digite a quantidade do produto cadastrado: "))
            produto = Produto(nome, preco, quantidade) #permite a criação de um produto novo (seguindo a ordem corretamente)
            produtos.append(produto)#adicionando a intancia de produto a lista de produtos
            print("Produto cadastrado com sucesso!")

        elif escolha == "2":
            if produtos:
                print("\nLista de Produtos Cadastrados:")
                for i, produto in enumerate(produtos, start=1):#cria uma enumeração,começando em 1 ate o ultimo produto para exibição
                    print(f"\nProduto {i}:")
                    produto.exibir_produto()
            else:
                print("Nenhum produto cadastrado.")

        elif escolha == "3":
            if produtos:
                for i, produto in enumerate(produtos, start=1):
                    print(f"{i}. {produto.nome}")# Exibe a lista de produtos com índice
                indice = int(input("Escolha o número do produto para atualizar o preço: ")) - 1
                #pede ao usuario que escolha um produto pelo numero
                if 0 <= indice < len(produtos): #faz uma verificação para saber se o indice é valido
                    novo_preco = float(input("Digite o novo preço do produto: "))
                    #solicita novo preço
                    produtos[indice].atualizar_preco(novo_preco)
                else:
                    print("Produto não encontrado.")
            else:
                print("Nenhum produto cadastrado.")

        elif escolha == "4":
            #identica a função 3, com a mudança de preço para quantidade
            if produtos:
                for i, produto in enumerate(produtos, start=1):
                    print(f"{i}. {produto.nome}")
                indice = int(input("Escolha o número do produto para atualizar a quantidade: ")) - 1
                if 0 <= indice < len(produtos):
                    nova_quantidade = int(input("Digite a nova quantidade do produto: "))
                    produtos[indice].atualizar_quantidade(nova_quantidade)
                else:
                    print("Produto não encontrado.")
            else:
                print("Nenhum produto cadastrado.")

        elif escolha == "5":#permite a finalização do sistema
            print("Saindo... Até logo!")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
            #quando o usuario selecionar uma opção invalida, exibirá essa mensagem e permitirá selecionar uma opção novamente

if __name__ == "__main__": #executa a função main de maneira externa ,facilitando mudanças no codigo.
    main_menu()
