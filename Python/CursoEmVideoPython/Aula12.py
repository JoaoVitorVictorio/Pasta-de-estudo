# Condiçoes aninhadas

nome = str(input('Qual é o seu nome? '))
if nome == 'João':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
else:
    print('Seu nome é legal!')
print('Tenha um bom dia, {}'.format(nome))
