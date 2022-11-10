# Exercício de criar um programa para saber o antecessor e o sucessor de um número
n1 = int(input('Digite um número: '))
n2 = -1
n3 = +1
a = int(n1) + int(+n2)
s = int(n1) + int(n3)
print('Analisando o valor: {}, seu antecessor é: {}, e o sucessor é: {}.'.format(n1, a, s))

# Primeiro método de print
n = int(input('Digite um número: '))
a = n - 1
s = n + 1
print('Analisando o valor: {}, seu antecessor é: {}, e o sucessor é: {}.'.format(n, a, s))

# Segundo método de print
n = int(input('Digite um número: '))
print('Analisando o valor: {}, seu antecessor é: {}, e o sucessor é: {}.'.format(n, (n-1), (n+1)))