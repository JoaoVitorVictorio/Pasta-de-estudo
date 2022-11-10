# Média de nota
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))
nota4 = float(input('Quarta nota: '))

resultado = (nota1 + nota2 + nota3 + nota4) / 4

print('Tirando {} , {} , {} e {}, a média do aluno é {:.1f}.'.format(nota1, nota2, nota3, nota4, resultado))

if resultado >= 7:
    print('O aluno está \033[32mAPROVADO!\033[m')

elif resultado > 5 and 6:
    print('O aluno está \033[34mRECUPERAÇÃO!\033[m')

else:
    print('O aluno está \033[31mREPROVADO!\033[m')

