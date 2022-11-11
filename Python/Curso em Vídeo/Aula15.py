# Interrompendo repetições while
cont = 1
while cont <= 10: # vai contar de 1 até a quantidade estabelecida.
    print(cont, '-> ', end='')
    cont += 1
print('Fim')

'''n = 0
while n != 999: # vai enquanto no número 999 não for digitado no terminal.
    n = int(input('Digite um número: '))'''

'''n = cont = 0
while cont < 3: # vai ler a quantidade de números vez estabelecida.
    n = int(input('Digite um número: '))
    cont += 1'''

'''c = n = s = 0
while True: # Testando a função break
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    c += 1
# print('Você digitou: {} números e a soma entre eles é: {}'.format(c, s))
print(f'Você digitou: {c} números e a soma entre eles é: {s}')# print utilizando f'strings'''

'''nome = 'João'
idade = 25
peso = 66
print(f'O {nome} tem {idade} anos e pesa {peso} kg.')'''
