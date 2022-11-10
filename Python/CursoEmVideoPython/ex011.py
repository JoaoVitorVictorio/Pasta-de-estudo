# Exercício de criar um programa para converter de R$ para US$
d = float(input('Qual valor é o valor que deseja converter? R$:'))
print('Com R${},você pode comprar US$:{:.2f}'.format(d,(d/3.27)))
