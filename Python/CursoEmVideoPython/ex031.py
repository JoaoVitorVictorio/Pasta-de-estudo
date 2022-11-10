# Exercício de Par ou ímpar
num = int(input('Me diga um número qualquer: '))
r = num % 2
if r == 0:
    print('O número {} é: PAR'.format(num))
else:
    print('O número {} é: ÍMPAR'.format(num))

