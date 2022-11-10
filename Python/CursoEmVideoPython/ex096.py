# Função que calcula área
def titulo(txt):
    print('-' * 50)
    print(txt)
    print('-' * 50)
def area(l, c):
    t = l * c
    print(f'A área de um terreno {l} x {c} é de = {t}m²')


titulo(f'{"CONTROLE DE TERRENO":^50}')
larg = float(input('Digite a largura do terreno (m): '))
comp = float(input('Digite o comprimento do terreno (m): '))
area(larg, comp)
print('-'*50)
