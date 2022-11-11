# Palpites para a Mega Sena
from random import randint
from time import sleep
lista = []
jogos = []
print('-'*50)
print(f'{"MEGA SENA!":^50}')
print('-'*50)
quantidade = int(input('Quantos jogos você deseja que eu sorteie? '))
print('='*50)
tot = 1
print(f'{f"GERANDO {quantidade} JOGOS":^50}')
print('=' * 50)
while tot <= quantidade:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for i, l in enumerate(jogos):
    sleep(1)
    print(f'Jogo {i+1}: {l}')
print()
print('-'*19, 'BOA SORTE!', '-'*19)





