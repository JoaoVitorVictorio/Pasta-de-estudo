# Estatísticas em produtos
print('-'*20)
print('   LOJA VICTORIO   ')
print('-'*20)
menorvalor = cont = maisdemil = totalcompra = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço R$: '))
    cont += 1
    totalcompra += preço
    continuar = ' '
    if preço > 1000:
        maisdemil += 1
    if cont == 1 or preço < menorvalor:
        menorvalor = preço
        barato = produto
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-'*50)
print(f'O total da sua compra foi de R$: {totalcompra:.2f}')
print(f'Temos {maisdemil} produtos custaram mais de R$: 1000.00')
print(f'E o produto mais barato foi {barato} que custou R${menorvalor:.2f}')



