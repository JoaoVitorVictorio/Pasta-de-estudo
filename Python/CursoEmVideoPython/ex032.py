# Custo de uma viagem
# Primeiro método
'''d = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de: {:.1f} Km.'.format(d))
p1 = (d * 0.50)
p2 = (d * 0.45)
if d <= 200:
    print('E o preço da sua passagem será de: R${:.2f}'.format(p1))
else:
    print('E o preço da sua passagem será de: R${:.2f}'.format(p2))'''

# Segundo método
distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de: {:.1f} Km.'.format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('E o preço da sua passagem será de: R${:.2f}'.format(preço))

