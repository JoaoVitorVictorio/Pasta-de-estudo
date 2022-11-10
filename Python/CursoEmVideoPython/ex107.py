# Formatando preços importando módulos
import uteis
preço = float(input('Digite o preço R$: '))
uteis.linha()
print(f'A metade de R${preço:.2f} é: R${uteis.metade(preço):.2f}')
print(f'O dobro de R${preço:.2f} é: R${uteis.dobro(preço):.2f}')
print(f'Aumentando 10% temos R${uteis.aumentar(preço, 10):.2f}')
print(f'Diminuindo 10% temos R${uteis.diminuir(preço, 10):.2f}')
uteis.linha()


