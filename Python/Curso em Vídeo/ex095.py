# Aprimorando os Dicionários
# Cadastro de Jogador de Futebol
time = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou?: '))
    partidas.clear()
    for c in range(1, tot+1):
        partidas.append(int(input(f' Quantos gols na {c}ª partida?: ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
        if continuar in 'SN':
            break
        else:
            print('Erro! Responda apenas S ou N.')
    if continuar == 'N':
        break
print('='*50)
print('CÓD ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*50)
for k, v in enumerate(time):
    print(f'{k + 1:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('='*50)
while True:
    busca = int(input('Exibir dados de qual jogador? (999 Finaliza o programa.): '))
    busca -= 1
    if busca == 998:
        break
    if busca >= len(time):
        print(f'Erro! Não foi possivel localizar jogador com este código {busca + 1}!')
    else:
        print(f'DADOS DO JOGADOR: {time[busca]["Nome"]}')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'    No {i+1}º jogo fez {g} gol')
print('*** PROGRAMA FINALIZADO ***')
