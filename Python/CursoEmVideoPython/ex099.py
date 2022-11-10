# Função que descobre o maior
from time import sleep
def linha():
    print('='*50)

def maior(* num):
    cont = maior = 0
    linha()
    print('Analisando os números...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados: {cont} números ao todo.')
    print(f'O maior número informado foi: {maior}')

maior(2, 6, 8, 7, 1, 4, 5, 3)
maior(4, 7, 0)
maior(1, 2)
maior()
