# Tuplas
# () Tuplas
# [] Lista
# {} Dicionario
# Tuplas são IMUTÁVEIS
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(sorted(lanche)) # Mostra os itens da variavel em ordem

print(lanche)
print(lanche[0])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-3:])
# print(len(lanche)) # função len diz quantos elementos tenho dentro da variavel

for comida in lanche: # Maneira mais simples se eu não precisar declarar a posição
    print(f'Vou comer {comida}')
print('Comi demais!')

for cont in range(0, len(lanche)): # Maneira utilizando o range para declarar a posição com len
    print(f'Vou comer {lanche[cont]} na posição {cont}')
print('Comi demais!')

for pos, comida in enumerate(lanche): # Maneira utilizando o enumerate para declarar a posição
    print(f'Vou comer {comida} na posição {pos}')
print('Comi demais!')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a
print(a)
print(b)
print(c)
print(d)
print(len(c))
print(len(a))
print(c.count(5)) # count mostra quantas vezes é exbido o resultado dentro da tupla
print(c.count(2))
print(c.index(8)) # index mostra qual é posição do resultado na tupla pegando a primeira ocorrencia
print(d.index(5, 1)) # index mostra qual é posição do resultado na tupla pegando a segunda ocorrencia

pessoa = ('João', 25, 'M', 66)# No pyton posso misturar tipos dentro de uma variavel
del(pessoa) # Função del apaga uma variavel
print(pessoa)

