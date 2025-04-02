import os

def criar_diretorio(nome_diretorio: str) -> None:
    try:
        os.makedirs(nome_diretorio)
        print(f"O diretorio '{nome_diretorio}' foi encontrado com sucesso.")
    except FileExistsError:
        print(f"O Diretório '{nome_diretorio}' ja existe.")
    except PermissionError:
        print(f"Ocorreu um erro ao criar o diretório '{nome_diretorio}'.")
    except Exception as e:
        print(f"Ocorreu um erro ao criar o diretorio '{nome_diretorio}': {e}")

def criar_arquivo(arquivo_nome: str, conteudo: str) -> None:
    try:
        with open (arquivo_nome, 'w') as file:
            file.write(conteudo)
        print(f"O arquivo '{arquivo_nome}' fi criado com sucesso.")
    except PermissionError:
        print(f"Permissão negada para criar o arquivo '{arquivo_nome}'.")
    except Exception as e:
        print(f"Ocorreu um erro ao criar o arquivo '{arquivo_nome}': {e}")

def main() -> None:
    diretorio_atual = os.getcwd()
    print(f"Caminho com os.getcwd(): '{diretorio_atual}'")
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    print(f"Caminho com os path: '{diretorio_atual}'")
    nome_diretorio = os.path.join(diretorio_atual, "diretorio_aula")
    arquivo_nome = os.path.join(nome_diretorio, "arquivo_aula.txt")
    conteudo = "Conteúdo de exemplo."

    try:
        criar_diretorio(nome_diretorio)
        criar_arquivo(arquivo_nome, conteudo)
    except FileNotFoundError:
        print("O caminho especifico não foi encontrado.")
    except PermissionError:
        print("permissao negada para cessar o caminho especificado.")
    except Exception as e:
        print(f"Ocorre um erro inesperado: {e}")


if __name__ == "__main__":
    main()
