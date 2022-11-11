# Progressão Aritmética
print('='*30)
print('     10 TERMOS DE UMA PA     ')
print('='*30)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (11 - 1) * razão
for cont in range(primeiro, décimo, razão):
    print('{}'.format(cont), end=' → ')
print('ACABOU')
