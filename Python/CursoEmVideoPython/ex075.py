# Maior e menor valores em Tupla
from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os números sorteador foram: ', end='')
for num in n:
    print(f'{num}', end=' ')
print(f'\nO maior número sorteado foi: {max(n)}')
print(f'O menor número sorteado foi: {min(n)}')

