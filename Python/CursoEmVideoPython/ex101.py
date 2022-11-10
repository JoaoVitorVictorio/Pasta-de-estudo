# Funções para votação
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: Não é possivel votar ainda'
    elif idade < 18 or idade > 65:
        return f'Com {idade} anos: O voto é opcional'
    else:
        return f'Com {idade} anos: O seu voto é obrigátorio.'


print('-'*70)
nasc = int(input('Digite seu ano de nascimento para verificar se já pode votar: '))
print(voto(nasc))

