# Boletim com listas compostas
from time import sleep
ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    if continuar in 'N':
        break
print('-'*30)
print(f'{"Nº.":<4}{"Nome":<10}{"Média":>8}')
print('-'*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*60)
    opc = int(input('Exibir notas de qual aluno(a)? (Digite: 999 finaliza o programa): '))
    if opc == 999:
        print('FINALIZANDO....')
        sleep(1)
        print('PROGRAMA FINALIZADO!')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são: {ficha[opc][1]}')
