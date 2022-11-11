# Estrutura de repetição while
'''for c in range(1, 11):
    print(c)
print('Fim')'''

'''c = 1
while c < 11:
    print(c)
    c = c + 1
print('Fim')'''

# Enquanto o valor for DIFERENTE de 0 o programa vai continuar pedindo um valor no input
'''n = 1
while n != 0:
    n = int(input('Digite um número: '))
print('Fim')'''

# Enquanto o valor for SIM o programa irá continuar rodando até que o valor sejá NÃO
'''r = 'S'
while r == 'S':
    n = str(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()
print('Fim')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print('Você digitou {} números pares e {} números impares'.format(par, impar))