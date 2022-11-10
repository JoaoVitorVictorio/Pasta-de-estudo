# Unindo dicionários e listas
galera = []
pessoa = {}
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Digite apenas M ou F: ')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('Erro! Digite S ou N.')
    if continuar == 'N':
        break
print('-'*45)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'B) A média de idade é de {média:5.2f} anos.')
print('C) As mulheres cadastradas foram: ', end='')
for f in galera:
    if f['sexo'] == 'F':
        print(f'{f["nome"]}', end=', ')
print()
print('D) Os homens cadastrados foram: ', end='')
for m in galera:
    if m['sexo'] == 'M':
        print(f'{m["nome"]}', end=', ')
print()
print('E) Lista de pessoas que estão com idade acima da média: ',end='')
for p in galera:
    if p['idade'] > média:
        print('     ',end='')
        print()
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
print()
print('<<< PROGRAMA FINALIZADO >>>')






