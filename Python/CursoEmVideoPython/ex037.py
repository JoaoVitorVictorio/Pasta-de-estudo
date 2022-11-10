valorcasa = float(input('Qual é o valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
parcelas = int(input('Deseja financiar em quantos anos? '))

prestação = valorcasa / (parcelas * 12)
mínimo = (salario * 30 /100)

print('Para pagar uma casa de R${:.2f}, em {} anos a prestação será de R${:.2f}.'.format(valorcasa, parcelas, prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser concedido!')
else:
    print('Infelizmente o empréstimo foi negado.')