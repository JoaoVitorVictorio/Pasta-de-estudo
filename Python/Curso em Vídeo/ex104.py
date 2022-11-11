# Validando entrada de dados em Python
# Primeiro método
def leiaInt(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            n = print(f'Você digitou o número: {n}')
            break
        else:
            n = print('\033[31mErro! Digite um número inteiro válido.\033[m')


n = leiaInt('Digite um número: ')


# Segundo método
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok =True
        else:
            n = print('\033[31mErro! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você digitou o número: {n}')