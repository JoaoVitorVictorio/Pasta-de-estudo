# Tratando vários valores v1.0
contador = 0
somador = 0
num = int(input('Digite um número (999 faz o programa parar): '))
while num != 999:
    contador = contador + 1
    somador = somador + num
    num = int(input('Digite um número (999 faz o programa parar): '))
if num == 999:
    print('Você digitou {} números e a soma entre eles foi {}.'.format(contador, somador))

