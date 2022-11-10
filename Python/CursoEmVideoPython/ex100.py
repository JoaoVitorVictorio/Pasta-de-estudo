# Funções para sortear e somar
from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 números: ')
    for c in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.3)


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'\nSomando os valores pares de {lista}, o resultado é de: {soma}')


num = []
sorteia(num)
somaPar(num)

