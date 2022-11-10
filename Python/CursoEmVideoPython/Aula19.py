# Dicionários
'''pessoas = {'nome': 'João', 'sexo': 'Masculino', 'idade': 25}
print(pessoas['nome'])
print(pessoas['idade'])
print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys()) # Exibi as chaves
print(pessoas.values()) # Exibi os valores
print(pessoas.items()) # Exibi as chaves com os valores

for k in pessoas.keys():
    print(k)

for v in pessoas.values():
    print(v)

# del pessoas['sexo']
# pessoas['nome'] = 'Leandro' # Para alterar o valor
pessoas['peso'] = 66.5
for k, v in pessoas.items():
    print(f'{k} = {v}')'''

'''brasil = []
estado1 = {'uf': 'São Paulo', 'sigla': 'SP'}
estado2 = {'uf': 'Parana', 'sigla': 'PR'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])'''

'''estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for v in e.values():
        print(v, end='')
    print()'''