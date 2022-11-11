# Funções (Parte 2)
# função help = mostra um manual de alguma função por exemplo:
#help(input)
# função .__doc__ = também mostra um manual de alguma função por exemplo:
#print(input.__doc__)

#docstring  = mostra um manual feito sobre uma função criada
'''def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: Inicio da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('Fim')


help(contador)
contador(1, 200, 5)'''

# Parametros opcionais:
'''def somar (a = 0, b = 0, c = 0):
    """
    -> Faz a soma de três números e mostra a resultado na tela
    :param a: O primeiro número
    :param b: O segundo número
    :param c: O terceiro número
    :return: Mostra o resultado das somas
    """
    r = a + b + c
    print(f'O resultado da soma de ({a} + {b} + {c}) é de: {r}')


somar(5, 10, 25)
somar(5, 4)
somar()'''

# Escopo de variáveis:
'''def função():
    global n1 # global pega o valor fora do escopo e coloca dentro
    # n1 = 4
    print(f'N1 dentro do escopo vale: {n1}')


n1 = 2
função()
print(f'N1 fora do escopo vale: {n1}')'''

# Retorno de valores:
'''def somar (a = 0, b = 0, c = 0):
    r = a + b + c
    return r


r1 = somar(5, 10, 25)
r2 = somar(5, 4)
r3 = somar(6)

print(f'Os resultados foram: {r1}, {r2}, e {r3}')'''

'''def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
#n = int(input('Digite um número: '))
#print(f'O fatorial de {n} é igual a: {fatorial(n)}')
print(f'Os resultados são: {f1}, {f2} e {f3}')'''

'''def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

n = int(input('Digite um número para verificar se é par ou ímpar: '))

if par(n):
    print('Este número é par')
else:
    print('Este número é ímpar')'''

