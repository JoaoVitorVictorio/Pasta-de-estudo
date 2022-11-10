# Soma de ímpares multiplos de três.
soma = 0
contador = 0
for num in range(1, 501, 2):
    if num % 3 == 0:
        contador = contador + 1
        soma = soma + num
print('A soma de todos os: {} valores solicitados é: {}'.format(contador, soma))
