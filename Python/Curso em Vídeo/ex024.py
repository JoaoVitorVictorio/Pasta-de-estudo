# Separando dígitos de um número
num = int(input('Informe um número: '))
und = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(und))
print('Dezena: {}'.format(dez))
print('Centena: {}'.format(cen))
print('Milhar: {}'.format(mil))
