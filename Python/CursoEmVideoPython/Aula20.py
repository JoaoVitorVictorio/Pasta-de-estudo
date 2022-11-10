# Funções (Parte 1)
def linhas(): # def cria uma função para se usar na rotina sem parametros
    print('-'*30)

def mensagem(msg): # Defini uma função com varios prints dentro, incluindo um alteravel com parametros
    print('-' * 30)
    print(msg)
    print('-' * 30)

# Testes
linhas()
print(f'{"João":^30}')
linhas()
linhas()
print(f'{"Vitor":^30}')
linhas()
linhas()
print(f'{"Victorio":^30}')
linhas()

print('-'*60)

mensagem(f'{"João":^30}')
mensagem(f'{"Vitor":^30}')
mensagem(f'{"Victorio":^30}')

def soma(a, b):
    s = a + b
    print(f'A soma de {a} + {b} = {s}')


soma(a=3, b=2)
soma(b=5, a=4)
soma(2, 5)
print('-'*60)
# Empacotar parametros
def contador(* num):
    for n in num:
        print(f'{n} ', end='')
    print('-> FIM')


contador(1, 2)
contador(1, 2, 3)
contador(1, 2, 3, 4)

print('-'*60)
def digitos(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo temos {tam} números.')


digitos(1, 2)
digitos(1, 2, 3)
digitos(1, 2, 3, 4)
print('-'*60)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
dobra(valores)
print(valores)
print('-'*60)

def soma(* núm):
    s = 0
    for n in núm:
        s += n
    print(f'Somando os valores {núm} temos {s}')

soma(1, 5)
soma(5, 3)
print('-'*60)

