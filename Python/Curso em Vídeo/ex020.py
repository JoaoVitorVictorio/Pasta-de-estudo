# Exercício de criar um programa para sortear um aluno aleatório
import random
al1 = str(input('Primeiro aluno: '))
al2 = str(input('Segundo aluno: '))
al3 = str(input('Terceiro aluno: '))
al4 = str(input('Quarto aluno: '))
lista = [al1, al2, al3, al4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
