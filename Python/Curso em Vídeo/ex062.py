# Progressão Aritmética v2.0
print('='*30)
print('     10 TERMOS DE UMA PA     ')
print('='*30)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} → '.format(termo), end='')
    termo = termo + razão
    cont = cont + 1
print('FIM')
