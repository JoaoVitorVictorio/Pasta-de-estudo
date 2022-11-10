# Exercício de criar um programa para saber o angulo do Seno, Cosseno e da Tangente convertendo em radiano
import math
a = float(input('Digite o ângulo que você deseja: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('O angulo de {} tem o SENO de {:.2f}'.format(a,s))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(a,c))
print('O angulo de {} tem o TANGENTE de {:.2f}'.format(a,t))


