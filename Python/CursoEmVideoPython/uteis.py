# Criando funçoes para pode importa-la em outra aba futuramente
def linha():
    print('-'*50)


def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f = f * c
    return f


def aumentar(preço=0, taxa=0, form=False):
    res = preço + (preço * taxa/100)
    return res if form is False else moeda(res)


def diminuir(preço=0, taxa=0, form=False):
    res = preço - (preço * taxa/100)
    return res if form is False else moeda(res)


def dobro(preço=0, form=False):
    res = preço * 2
    return res if form is False else moeda(res)


def metade(preço=0, form=False):
    res = preço / 2
    return res if form is False else moeda(res)


def triplo(preço=0):
    res = preço * 3
    return res


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço=0, taxaa=10, taxar=5):
    print('-'*40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('-'*40)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'A metade do preço: \t{metade(preço, True)}')
    print(f'O dobro do preço: \t{dobro(preço, True)}')
    print(f'{taxaa}%: de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de redução:\t\t{diminuir(preço, taxar, True)}')
    print('-' * 40)


def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[31mErro! "{entrada}" é um preço inválido\033[m')
        else:
            válido = True
            return float(entrada)


def inteiro(msg):
    while True:
        try:
            numi = int(input(msg))
        except(ValueError, TypeError):
            print(f'\033[31mErro! Por favor digite um número inteiro válido!\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return numi


def real(msg):
    while True:
        try:
            numr = float(input(msg))
        except(ValueError, TypeError):
            print(f'\033[31mErro! Por favor digite um número inteiro válido!\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return numr
