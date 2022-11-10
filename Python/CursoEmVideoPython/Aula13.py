# Estrutura de repetição for
'''for c in range(0, 6): # Repetição de print na quantidade desejada
    print('Olá')
print('Fim')'''

'''for num in range(1, 11): # Contagem normal...
    print(num)
print('FIM')'''

'''for num in range(10, 0, -1): # Contagem de para trás
    print(num)
print('FIM')'''

'''for num in range(0, 7, 2): # Conta de 0 a 6 de 2 em 2
    print(num)
print('FIM')'''

'''n = int(input('Digite um número: ')) # Faz uma contagem de acordo com o número adicionado no input
for c in range(0, n+1):
    print(c)
print('FIM')'''

'''i = int(input('Início: ')) # Cria um passo a passo de instruçoes para execução
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')'''

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s = s + n
print('A soma de todos os valores é igual a: {}'.format(s))

