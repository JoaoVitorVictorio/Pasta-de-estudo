# Exercício de criar um programa para sortear alunos aleatórios em ordens aleatórias
# Primeiro método
import random
al1 = str(input('Primeiro aluno: '))
al2 = str(input('Segundo aluno: '))
al3 = str(input('Terceiro aluno: '))
al4 = str(input('Quarto aluno: '))
lista = [al1, al2, al3, al4]
random.shuffle(lista)
print('A ordem de apresentação será:')
print(lista)

# Segundo método
from random import shuffle
al1 = str(input('Primeiro aluno: '))
al2 = str(input('Segundo aluno: '))
al3 = str(input('Terceiro aluno: '))
al4 = str(input('Quarto aluno: '))
lista = [al1, al2, al3, al4]
shuffle(lista)
print('A ordem de apresentação será:')
print(lista)
