#  Análise de dados do grupo
from datetime import date
sexof = sexom = tot18 = cont = 0
print('-'*30)
print('   CADASTRE UMA PESSOA   ')
print('-'*30)
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('-' * 30)
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        sexom += 1
    if sexo == 'F' and idade < 20:
        sexof += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
    print('-' * 30)
print(f'Total de pessoas maiores de 18 anos: {tot18}.')
print(f'Ao todo temos: {sexom} homens cadastrados.')
print(f'E temos {sexof} mulheres com menos de 20 anos.')


