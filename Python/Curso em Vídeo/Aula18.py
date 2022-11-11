# Listas (Parte 2)
'''teste = []
teste.append('João')
teste.append(25)
pessoas = []
pessoas.append(teste[:])
teste[0] = 'Nayra'
teste[1] = 24
pessoas.append(teste[:])
print(pessoas)'''

'''pessoas = [['João', 25], ['Nayra', 24], ['Pedro', 17], ['Vera', 40]]
#print(pessoas[0][1])
#print(pessoas[1])
#print(pessoas[2])
#print(pessoas[3])
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade.')'''

pessoas = []
dados = []
totalmenor = totalmaior = 0
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    pessoas.append(dados[:])
    dados.clear()
for p in pessoas:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade já tem {p[1]}')
        totalmaior += 1
    else:
        print(f'{p[0]} ainda é menor de idade só tem {p[1]} anos')
        totalmenor += 1
print(f'Temos {totalmaior} maiores de idades e {totalmenor} menores de idade.')
