# classe para produtos com atributos (nome, preco, quantidade)

class Produto: #inicia a classe produto
    def __init__(self, nome: str, preco: float, quantidade: int) -> None: #construtor da classe produto
        self.nome = nome #args da classe
        self.preco = preco
        self.quantidade = quantidade

    def exibir_produto(self) -> None: #função para exibir as informações do produto
        print("Informações do produto!")
        print(f"nome: {self.nome}")
        print(f"preço: {self.preco}")
        print(f"Quantidade disponível: {self.quantidade}")

    def atualizar_preco(self, novo_preco: float) -> None:
        #função que permite a atualização do campo de "preço" de um produto
        #trata condição evitando valor negativo
        if novo_preco > 0 :
            self.preco = novo_preco #faz a alteração do campo preço do produto selecionado
            print(f"preço atualizado para {self.preco}")
        else:
            print("O preço precisa ser maior que zero!")

    def atualizar_quantidade(self, nova_quantidade: int) -> None:
        #função para atualizar quantidade de um produto ja cadastrado na lista
        if nova_quantidade > 0: #precisa ser maior que zero
            self.quantidade = nova_quantidade #adiciona uma nova quantidade ao produto selecionado
            print(f"A quantidade foi atualizada!")
            print(f"Quantidade: {nova_quantidade}")
        else: #não permite que o usuario insira valores negativos!
            print("Quantidade precisa ser maior que zero!")



