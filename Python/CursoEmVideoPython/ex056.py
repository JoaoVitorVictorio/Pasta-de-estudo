# Maior e menor da sequência
maiorpeso = 0
menorpeso = 0
for pessoa in range(1, 6):
    peso = float(input('Digite o peso da {}° pessoa (Kg): '.format(pessoa)))
    if pessoa == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso
print('O MAIOR peso lido foi de {}kg'.format(maiorpeso))
print('O MENOR peso lido foi de {}kg'.format(menorpeso))
