# Tabuada v2.0
num = int(input('Digite um número para vizualizar sua tabuada: '))
for cont in range(1, 11):
    print('{} x {:2} = {}'.format(num, cont, num*cont))