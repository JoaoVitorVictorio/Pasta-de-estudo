# Tuplas com Times de Futebol
print('=-' * 100)
times = ('Palmeiras', 'Internacional', 'Fluminense', 'Flamengo', 'Corinthians', 'Atletico-PR', 'Atlécito-MG',
        'América-MG', 'Goiáis', 'Botafogo', 'Santos', 'Bragantino', 'São Paulo', 'Fortaleza', 'Ceará-SC', 'Coritiba',
         'Avai', 'Cuiabá', 'Atletico-Go', 'Juventudo')
print(f'Lista de times do Brasileirão: {times}')
print('=-' * 100)
print(f'Os 5 primeiros são: {times[0:5]}')
print('=-' * 100)
print(f'Os 4 últimos são: {times[-4:]}')
print('=-' * 100)
print(f'Times em ordem alfábética: {sorted(times)}')
print('=-' * 100)
print(f'O São Paulo está na {times.index("São Paulo")+1}ª posição')

