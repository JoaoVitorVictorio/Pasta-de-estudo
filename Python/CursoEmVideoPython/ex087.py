# Mais sobre Matriz em Python
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = maiorvalor = somacolunas = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um número para [{linha}, {coluna}]: '))
print('='*30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            somapares += matriz[linha][coluna]
    print()
print('='*30)
print(f'A soma dos números pares é: {somapares}.')
for linha in range(0, 3):
    somacolunas += matriz[linha][2]
print(f'A soma da terceira coluna é: {somacolunas}.')
for coluna in range(0, 3):
    if coluna == 0:
        maiorvalor = matriz[1][coluna]
    elif matriz[1][coluna] > maiorvalor:
        maiorvalor = matriz[1][coluna]
print(f'O maior número da segunda linha é: {maiorvalor}.')
