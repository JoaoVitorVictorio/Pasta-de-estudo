# Listas (Parte 1)
# listas são mutáveis
'''num = [2, 5, 9, 1]
num[0] = 6
num[1] = 2
num.append(7) # append serve para adicionar um valor no ultimo elemento da lista
num.sort() # sort deixa os elementos em ordem crescente
num.sort(reverse=True) # sort(reverse=True) Deixa os elementos em ordem decrecente
num.insert(2, 0) # Insere um número entre os elementos conforme defenido entre parenteses
num.pop() # Se utilizar o .pop sem parametro vai remover o ultimo elemento da lista
num.pop(2) # Se utilizar o .pop com paramentro vai remover o elemento da lista
num.remove(2)# Remove o primeiro número definido como parametro da lista
if 5 in num:
    num.remove(5)
else:
    print('Não foi localizado o número 5')
print(num)
print(f'Essa lista tem {len(num)} elementos') # Utilizando o len para saber quantos elementos tem na lista'''

'''valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores:
    print(f'{v}...', end=' ')'''

'''valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')'''

'''valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Fim da lista.')'''

'''a = [1, 2, 3, 4, 5,]
b = a[:] # [:] Cria uma cópia de uma lista
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')'''
