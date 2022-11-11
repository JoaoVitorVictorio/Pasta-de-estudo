# Listas com pares e ímpares
num = [[], []]
valor = 0
for c in range(1, 8):
    valor = (int(input(f'Digite o {c}º número: ')))
    if valor % 2 == 0:
        num[0].append(valor)
    elif valor % 2 == 1:
        num[1].append(valor)
print('=' * 55)
num[0].sort()
num[1].sort()
print(f'Os números PARES digitados foram: {num[0]}')
print(f'Os números ÍMPARES digitados foram: {num[1]}')
