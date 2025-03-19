caminho_arquivo = 'nomes.txt'

arquivo = open(caminho_arquivo, 'a')
arquivo.write('victor\n')
arquivo.close()
arquivo = open(caminho_arquivo, 'r')
linhas = arquivo.readlines()
for i, linha in enumerate(linhas, start=1):
    print(f'linha {i}: {linha}')
