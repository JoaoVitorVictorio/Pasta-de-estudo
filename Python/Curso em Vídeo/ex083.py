# Dividindo valores em várias listas
num = []
pares = []
ímpares = []
while True:
    num.append(int(input('Digite um número: ')))
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar in 'N':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        ímpares.append(v)
print('-=' * 30)
print(f'A lista completa é: {num}')
print(f'A lista de pares é: {pares}')
print(f'A lista de ímpares é {ímpares}')





