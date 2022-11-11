# Soma dos números pares
soma = 0
contador = 0
for c in range(1, 7):
    num = int(input('Digite o {} número: '.format(c)))
    if num % 2 == 0:
        soma = soma + num
        contador = contador + 1
print('Você informou {} números pares e a soma de todos eles foi: {}'.format(contador, soma))
 
