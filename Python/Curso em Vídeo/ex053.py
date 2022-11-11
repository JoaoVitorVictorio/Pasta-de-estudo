# Números primos
n = int(input('Digite um número: '))
total = 0
for cont in range(1, n + 1):
    if n % cont == 0:
        print('\033[33m', end='')
        total = total + 1
    else:
        print('\033[31m', end='')
    print('{} '.format(cont), end= '')
print('\n\033[mO número {} foi divisível: {} vezes.'.format(n, total))
if total == 2:
    print('Sendo assim ele é PRIMO!')
else:
    print('Sendo assim ele NÃO É PRIMO!')
