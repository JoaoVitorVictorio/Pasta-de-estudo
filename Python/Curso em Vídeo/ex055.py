# Grupo de maioridade
from datetime import date
contmaior = 0
contmenor = 0
for pessoas in range(1, 8):
    nascimento = int(input('Em que ano a {}° pessoa nasceu? '.format(pessoas)))
    idade = (date.today().year - nascimento)
    if idade >= 21:
        contmaior = contmaior + 1
    else:
        contmenor = contmenor + 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(contmaior))
print('E tivemos {} que ainda são menores de idade.'.format(contmenor))
