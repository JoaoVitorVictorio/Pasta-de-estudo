# Contando vogais em Tupla
palavras = ('aprender', 'estudar', 'programar', 'linguagem',
            'trabalhar', 'dedicar', 'praticar',
            'futuro', 'desenvolvedor', 'mercador', 'curso',
            'faculdade', 'prova')
print('-'*40)
print(f'{"VERIFICANDO VOGAIS NAS PALAVRAS":^40}')
print('-'*40)
for p in palavras:
    print(f'\nNa palavra {p} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
