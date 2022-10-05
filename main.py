# Buscador de arquivos 
# OS - Percorrendo arquivos e pastas

import os
from utils import formata_tamanho

diretorio = input("Digite o diretório para pesquisa: ")
palavra_chave = input("Digite a palavra-chave: ")


cont = 0
# Walk = Caminha entre os arquivos
for raiz, diretorios, arquivos in os.walk(diretorio):
    for arquivo in arquivos:
        if palavra_chave in arquivo:
            try:
                cont += 1
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho_arquivo = os.path.getsize(caminho_completo)
                
                print()
                print('Encontrei o arquivo: ', arquivo)
                print('Diretório: ', caminho_completo)
                print('Nome do arquivo: ', nome_arquivo)
                print('Extenção: ', ext_arquivo)
                print('Tamanho: ', tamanho_arquivo)
                print('Tamanho formatado: ', formata_tamanho(tamanho_arquivo))
            except PermissionError as e:
                print('Sem permissão neste arquivo.')
            except FileNotFoundError as e:
                print('Arquivo não encontrado.')
            except Exception as e:
                print('Erro desconhecido.', e)
print()
if cont == 0 or cont == 1:
    print(f'{cont} arquivo encontrado')
else:
    print(f'{cont} arquivos encontrados')