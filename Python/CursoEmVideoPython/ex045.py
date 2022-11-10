# Gerenciamento de pagamentos
preço = float(input('Preço das compras: R$ '))

print('''FORMAS DE PAGAMENTO:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opção = int(input('Qual é a opção? '))

if opção == 1:
    total = preço - (preço * 10 / 100)

elif opção == 2:
    total = preço - (preço * 5 / 100)

elif opção == 3:
    total = preço
    parcelamento = total / 2
    print('Sua compra será parcelada em 2x de {:.2f} SEM JUROS'.format(parcelamento))

elif opção == 4:
    total = preço + (preço * 20 / 100)
    totalparcelas = int(input('Quantas parcelas? '))
    parcelamento = total / totalparcelas
    print('Sua compra será parcelada em {}x de {:.2f} COM JUROS'.format(totalparcelas, parcelamento))

else:
    total = preço
    print('\033[31mOpção inválida de pagamento, tente novamente!\033[m')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, total))

