# Cadastro de Jogador de Futebol
jogador = {}
partidas = []
jogador['Nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou?: '))
for c in range(1, tot+1):
    partidas.append(int(input(f' Quantos gols na {c}ª partida?: ')))
jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)
print('-'*50)
print(f'O jogador {jogador["Nome"]} jogou: {tot} partidas.')
for i, v in enumerate(jogador['Gols']):
    print(f'    -> Na {i+1}ª partida, fez {v} gol.')
print(f'Totalizando {jogador["Total"]} gols.')
