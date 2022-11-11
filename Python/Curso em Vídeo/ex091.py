# Jogo de Dados em Python
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'João': randint(1, 6),
        'Vera': randint(1, 6),
        'Pedro': randint(1, 6),
        'Nayra': randint(1, 6)}
ranking = ()
for k, v in jogo.items():
    print(f'{k} tirou: {v} no dado.')
    sleep(1)
print('-'*40)
print(f'{"<<< RANKING DOS JOGADORES >>>":^40}')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    sleep(1)
    print(f'{i + 1}º lugar: {v[0]} que tirou: {v[1]} no dado.')
print('-'*40)
