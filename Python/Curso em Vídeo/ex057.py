# Analisador completo
somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
mulher20 = 0
for dados in range(1, 5):
    print('----- {}ª PESSOA -----'.format(dados))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    somaidade = somaidade + idade
    if dados == 1 and sexo in 'M m':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'M m' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'F f' and idade < 20:
        mulher20 = mulher20 + 1
médiaidade = somaidade / 4
print('A média de idade do grupo é de {:.2f} anos'.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulher com menos de 20 anos'.format(mulher20))

