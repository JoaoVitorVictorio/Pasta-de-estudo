# Cálculo do Fatorial

'''from math import factorial
num = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(num)
print('O fatorial de {} é: {}'.format(num, f))'''

num = int(input('Digite um número para calcular seu fatorial: '))
contador = num
f = 1
print('Calculando {}! = '.format(num), end='')
while contador > 0:
    print('{}'.format(contador), end='')
    print (' x ' if contador > 1 else ' = ', end='')
    f = f * contador
    contador = contador - 1
print('{}'.format(f))
