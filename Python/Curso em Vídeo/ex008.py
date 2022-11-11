# Exercício de criar um programa para saber a média de uma nota de um aluno número.
n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
m = (n1 + n2) / 2
print('A média entre {:.1f} e {:.1f} é igual a: {:.1f}'.format(n1,n2,m))