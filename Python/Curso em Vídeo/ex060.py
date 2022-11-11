# Criando um Menu de Opções
from time import sleep
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
opção = 0
while opção != 5:
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa''')
    opção = int(input('>>>> Qual é a sua opção? '))
    if opção == 1:
        soma = num1 + num2
        print('A soma entre {} e {} é: {}'.format(num1, num2, soma))
    elif opção == 2:
        multiplicar = num1 * num2
        print('A multiplicação entre {} e {} é: {}'. format(num1, num2, multiplicar))
    elif opção == 3:
        if num1 > num2:
            maior = num1
            print('Entre {} e {} o maior valor é: {}'.format(num1, num2, maior))
        elif num2 > num1:
            maior = num2
            print('Entre {} e {} o maior valor é: {}'.format(num1, num2, maior))
    elif opção == 4:
        print('Informe os números novamente:')
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
        sleep(2)
        print('Fim do programa, volte sempre!')
    else:
        print('Opção inválida, tente novamente.')
    print('---' * 15)
