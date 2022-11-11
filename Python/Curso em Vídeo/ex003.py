#Função input com contas + print com .format
# Primeiro método
num1 = input('Digite o primeiro número para somar: ')
num2 = input('Agora digite o segundo número para somar com o primeiro: ')
soma = int(num1) + int(num2)
print('O resultado da soma dos dois números é: ', soma)

# Segundo método
n1 = int(input('Digite o primeiro número para somar: '))
n2 = int(input('Agora digite o segundo número para somar com o primeiro: '))
soma = n1 + n2
print('A soma entre {} e {} é igual a: {}'.format(n1, n2, soma))
