# Exercício de criar um programa para saber o custo em alugar um veículo
dias = float(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
pdia = dias * 60
pkm = km * 0.15
total = pdia + pkm
print('O total a pagar é de R${:.2f}'.format(total))




