# Game: Pedra, papel e tesoura
from random import randint
from time import sleep

# Primeiro método
itens = ('Pedra', 'Papel', 'Tesoura')
print('''Das opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
computador = randint(0, 2)
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
sleep(1)
print('=-'*15)
print('O Computador escolheu: {}'.format(itens[computador]))
print('O Jogador escolheu: {}'.format(itens[jogador]))
print('=-' * 15)
if jogador == computador:
    print('\033[33mEMPATE\033[m')
elif jogador == 0 and computador == 1:
    print('\033[31mO COMPUTADOR VENCEU\033[m')
elif jogador == 1 and computador == 2:
    print('\033[31mO COMPUTADOR VENCEU\033[m')
elif jogador == 2 and computador == 0:
    print('\033[31mO COMPUTADOR VENCEU\033[m')
elif computador == 0 and jogador == 1:
    print('\033[32mO JOGADOR VENCEU\033[m')
elif computador == 1 and jogador == 2:
    print('\033[32mO JOGADOR VENCEU\033[m')
elif computador == 2 and jogador == 0:
    print('\033[32mO JOGADOR VENCEU\033[m')
else:
    print('Opção Inválida')

# Segundo método
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Das opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
sleep(1)
print('=-'*15)
print('O Computador escolheu: {}'.format(itens[computador]))
print('O Jogador escolheu: {}'.format(itens[jogador]))
print('=-' * 15)
if computador == 0:
    if jogador == 0:
        print('\033[33mEMPATE\033[m')
    elif jogador == 1:
        print('\033[32mO JOGADOR VENCEU\033[m')
    elif jogador == 2:
        print('\033[31mO COMPUTADOR VENCEU\033[m')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:
    if jogador == 0:
        print('\033[31mO COMPUTADOR VENCEU\033[m')
    elif jogador == 1:
        print('\033[33mEMPATE\033[m')
    elif jogador == 2:
        print('\033[32mO JOGADOR VENCEU\033[m')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:
    if jogador == 0:
        print('\033[32mO JOGADOR VENCEU\033[m')
    elif jogador == 1:
        print('\033[31mO COMPUTADOR VENCEU\033[m')
    elif jogador == 2:
        print('\033[33mEMPATE\033[m')
    else:
        print('JOGADA INVÁLIDA')
