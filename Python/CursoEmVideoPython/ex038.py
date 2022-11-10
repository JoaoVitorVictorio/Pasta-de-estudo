# Conversor de bases numéricas
base = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases abaixo para conversão
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))

if opção == 1:
    print('{} convertido para BINÁRIO é igual a: {}'.format(base, bin(base)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a: {}'.format(base, oct(base)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a: {}'.format(base, hex(base)[2:]))
else:
    print('Opção inválida, digite uma das opções acima')


