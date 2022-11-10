# Análise de dados em uma Tupla
num = (int(input('Digite um número: ')),
int(input('Digite outro número: ')),
int(input('Digite mais número: ')),
int(input('Digite o último número: ')))
print(f'Você digitou os números {num}')
print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('O número 3 não foi encontrado em nenhuma posição')
print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')

