# Lista composta e análise de dados
dados = []
principal = []
maiorpeso = menorpeso = pessoas = 0
while True:
    dados.append(str(input('Nome: ')).strip())
    dados.append(float(input('Peso: ')))
    if len(principal) == 0:
        maiorpeso = menorpeso = dados[1]
    else:
        if dados[1] > maiorpeso:
            maiorpeso = dados[1]
        if dados[1] < menorpeso:
            menorpeso = dados[1]
    principal.append(dados[:])
    dados.clear()
    continuar = str(input('Deseja continuar? [S/N]: ').strip().upper()[0])
    pessoas += 1
    if continuar in 'N':
        break
print('-' * 60)
print(f'Ao todo, foram cadastradas {pessoas} pessoas.')
print(f'O maior peso foi de {maiorpeso}Kg. Peso de ',end='')
for p in principal:
    if p[1] == maiorpeso:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {menorpeso}Kg. Peso de ',end='')
for p in principal:
    if p[1] == menorpeso:
        print(f'[{p[0]}]', end=' ')

