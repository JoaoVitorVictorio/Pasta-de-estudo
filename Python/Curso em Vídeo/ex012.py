# Exercício de criar um programa para saber a dimensão de uma parede e quantos litros de tintas vou precisar utilizar para pinta-la
# Primeiro método
comp = float(input('Comprimento da parede: '))
alt = float(input('Altura da parede:'))
area = comp * alt
tinta = area / 2
print('Sua parede tem a dimenção de {}x{} e sua área é de {}m².'.format(comp,alt,area))
print('Para pintar está parede, você precisará de {}l de tinta.'.format(tinta))

# Segundo método
print('Sua parede tem a dimenção de {}x{} e sua área é de {}m².'.format(comp,alt,(comp*alt)))
print('Para pintar está parede, você precisará de {}l de tinta.'.format((comp*alt)/2))

