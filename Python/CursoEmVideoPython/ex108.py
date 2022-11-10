# Formatando Moedas em Python
import uteis
preço = float(input('Digite o preço R$: '))
uteis.linha()
print(f'A metade de {uteis.moeda(preço)} é: {uteis.moeda(uteis.metade(preço))}')
print(f'O dobro de {uteis.moeda(preço)} é: {uteis.moeda(uteis.dobro(preço))}')
print(f'Aumentando 10% temos: {uteis.moeda(uteis.aumentar(preço, 10))}')
print(f'Diminuindo 10% temos: {uteis.moeda(uteis.diminuir(preço, 10))}')
uteis.linha()


