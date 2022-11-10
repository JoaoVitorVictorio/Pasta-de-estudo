# Cadastro de Trabalhador em Python
from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['CTPS'] = int(input('Nº da carteira de trabalho (0 se não tiver): '))
if dados['CTPS'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-'*45)
for k, v in dados.items():
    print(f' - {k}: {v}')
print('-'*45)

