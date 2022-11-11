# Exercício de criar um programa para saber o dobro, o triplo e a raiz quadrada de um número.
# Primeiro método
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}. \nO triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, d, n, t, n, r))

# Segundo método
n = int(input('Digite um número: '))
print('O dobro de {} vale {}. \nO triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*2), n, (n*3), n, (n**(1/2))))




