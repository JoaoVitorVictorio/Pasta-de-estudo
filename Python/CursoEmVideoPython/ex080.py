# Valores únicos em uma Lista
números = list()
while True:
    n = int(input('Digite um número: '))
    if n not in números:
        números.append(n)
        print('Número adicionado com sucesso...')
    else:
        print('Valor duplicado não será adicionado!')
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'S':
        continue
    else:
        print('=-=' * 15)
        print(f'Você adicionou os números: {sorted(números)}')
        break
