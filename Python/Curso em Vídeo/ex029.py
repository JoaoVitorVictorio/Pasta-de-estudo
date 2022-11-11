# Jogo de adivinhação
from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 18)
print('Vou pensar em um número entre 0 e 5, tente adinhar...')
print('-=-' * 18)
jogador = int(input('Em que número eu pensei: '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Opa, você conseguiu acerta!')
else:
    print('Você errou, eu pensei no {} e não no {}!'.format(computador, jogador))
