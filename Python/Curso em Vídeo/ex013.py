# Exercício de criar um programa para quanto o produto vai custar com o desconto.
p = float(input('Qual é o preço do produto? R$: '))
d = p*0.95
print('O produto que custava R${:.2f}, na promoção com deconto de 5% vai custar R${:.2f}.'.format(p, d))
