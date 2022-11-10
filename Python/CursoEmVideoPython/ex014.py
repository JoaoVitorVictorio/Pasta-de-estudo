# Exercício de criar um programa para saber quanto o funcionário irá receber de aumento
s = float(input('Qual é o salário do funcionário? R$: '))
a = (s*0.15)+s
print('Um funcionário que ganhava R$:{:.2f}, com 15% de aumento passa a receber R${:.2f}.'.format(s, a))