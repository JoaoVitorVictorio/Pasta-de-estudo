# Exercício de criar um programa para saber o valor inteiro exato de um número.
# Primeiro método
import math
v = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(v,math.trunc(v)))

# Segundo método
from math import trunc
v = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(v,trunc(v)))

# Terceiro método
v = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(v, int(v)))



