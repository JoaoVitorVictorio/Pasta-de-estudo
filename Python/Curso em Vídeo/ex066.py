# Maior e Menor valores
continuar = 'S'
contador = soma = quantidade = média = maior = menor = 0
while continuar in 'S':
    n = int(input('Digite um número: '))
    continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    contador = contador + 1
    soma = soma + n
    quantidade = quantidade + 1
    média = soma / quantidade
    if quantidade == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('Você digitou {} números e a média entre eles é: {}'.format(contador, média))
print(('O MAIOR valor foi: {} e o MENOR foi: {}'.format(maior, menor)))

