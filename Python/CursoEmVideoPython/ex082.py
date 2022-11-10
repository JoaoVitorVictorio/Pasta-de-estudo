# Extraindo dados de uma Lista
valores = []
elementos = 0
while True:
    valores.append(int(input('Digite um número: ')))
    elementos += 1
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar in 'N':
        break
print('=-=' * 30)
print(f'Você digitou {elementos} elementos.')
valores.sort(reverse=True)
print(f'Os números digitados em ordem decrescente são: {valores}')
if 5 in valores:
    print('O número 5 faz parte da lista!')
else:
    print('O número 5 não foi encontrado nesta lista!')



