# Alistamento militar
from datetime import date
ano = int(input('Ano de nascimento: '))
sexo = str(input('Você é do sexo masculino ou feminino: '))

idade = date.today().year - ano
alistamento = idade - 18
dataalistamento = date.today().year - alistamento

if sexo in 'Feminino feminino Mulher mulher Menina menina Masculino masculino Homem homem':
    print('Você não precisa fazer o alistamento militar obrigatório')

elif idade > 18:
    print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, (date.today().year)))
    print('Você deveria ter se alistado há {} anos.'.format(alistamento))
    print('Seu alistamento foi em {}'.format(dataalistamento))

elif idade == 18:
    print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, (date.today().year)))
    print('Você tem que se alistar IMEDIATAMENTE')

elif idade < 18:
    print('Quem nasceu em {} tem {} ano(s) em {}.'.format(ano, idade, (date.today().year)))
    print('Ainda falta {} anos para você se alistar'.format(18 - idade))