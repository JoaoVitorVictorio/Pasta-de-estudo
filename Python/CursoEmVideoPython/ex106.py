# Interactive helping system in Python
from time import sleep
c = ('\033[m',
     '\033[0;30;41m',
     '\033[0;30;42m',
     '\033[0;30;43m',
     '\033[0;30;44m',
     '\033[0;30;45m',
     '\033[7;30'
     );


def ajuda(com):
    título(f'Acessando o manual do comando\'{com}\'', 4)
    print(c[3], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('-'*tam)
    print(f'  {msg}')
    print('-'*tam)
    print(c[0], end='')
    sleep(1)


comando = ''
while True:
    título('SISTEMA DE AJUDA PyHelp', 2)
    print('Digite FIM caso queira finalizar o programa')
    comando = str(input('Função ou Biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('PROGRAMA FINALIZADO', 1)
