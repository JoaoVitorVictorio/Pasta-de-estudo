# Validação de Dados
gênero = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
while gênero not in 'M m F f':
    gênero = str(input('Dados inválidos. Por favor, digite um seu sexo: ')).upper().strip()[0]
if gênero == 'M':
    print('Gênero \033[034m{}\033[m registrado com sucesso'.format(gênero))
else:
    print('Gênero \033[031m{}\033[m registrado com sucesso'.format(gênero))