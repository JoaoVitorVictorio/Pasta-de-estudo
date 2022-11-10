# Formatando Moedas em Python
import uteis
preço = float(input('Digite o preço R$: '))
uteis.linha()
print(f'A metade de {uteis.moeda(preço)} é: {uteis.metade(preço, True)}')
print(f'O dobro de {uteis.moeda(preço)} é: {uteis.dobro(preço, True)}')
print(f'Aumentando 10% temos: {uteis.aumentar(preço, True, 10)}')
print(f'Diminuindo 13% temos: {uteis.diminuir(preço, True, 13)}')
uteis.linha()


