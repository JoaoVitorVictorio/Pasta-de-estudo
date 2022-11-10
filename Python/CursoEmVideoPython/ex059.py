from random import randint
computador = randint(0, 10)
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
acertou = False
tentativas = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite?: '))
    tentativas = tentativas + 1
    if jogador == computador:
        acertou = True
        print('\033[36mIsso o número que eu pensei foi o {} e você acertou com {} tentativas. Parabéns!\033[m'.format(computador, tentativas))
    elif computador > jogador:
        print('Mais...')
    else:
        print('Menos...')
