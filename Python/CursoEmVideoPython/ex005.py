# Exercício de criar um programa para somar, multiplicar, dividir, potenciar um número.
n1 = int(input('Digite um valor: '))
n2 = int(input('Agora digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
p = n1 ** n2
di = n1 // n2
r = n1 % n2
# Primeiro método de print
'''print('A soma de {} + {} é igual a: {}'.format(n1,n2,s))
print('A multiplicação de {} + {} é igual a: {}'.format(n1,n2,m))
print('A divisão de {} + {} é igual a: {}'.format(n1,n2,d))
print('A potenciação de {} + {} é igual a: {}'.format(n1,n2,p))
print('A divisão real de {} + {} é igual a: {}'.format(n1,n2,di))
print('O resto da divisão de {} + {} é igual a: {}'.format(n1,n2,r))'''

# Segundo método de print
'''print('A soma é: {}, A multiplicação é: {}, A divisão é: {}, '.format(s, m, d), end='')
print('A potenciação é: {}, A divisão inteira é: {}, E o resto da divisão é: {}'.format(p, di, r))'''

# Terceiro método de print
'''print('A soma é: {}, \nA multiplicação é: {}, \nA divisão é: {}, \nA potenciação é: {}, \nA divisão inteira é: {}, \nE o resto da divisão é: {}'.format(s, m, d, p, di, r))'''
