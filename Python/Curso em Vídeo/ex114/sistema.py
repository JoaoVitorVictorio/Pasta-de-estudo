# Criando um menu
from ex114.lib.interface import *
from ex114.lib.arquivo import *
from time import sleep

arq = 'curso.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Digite o nome: '))
        idade = leiaInt('Digite a idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo')
        break
    else:
        print('\033[31mErro! Digite uma opção válida!\033[m')
    sleep(2)
