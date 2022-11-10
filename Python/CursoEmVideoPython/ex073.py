# Número por Extenso
n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
       'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 a 20: '))
    if num < 0 or num > 20:
        print('Número inválido. ', end='')
        continue
    if 0 <= num <= 20:
        print(f"Você digitou o número: {n[num]}")
        continuar = str(input('Você quer continuar [S/N]: ')).strip().upper()[0]
        if continuar in 'S':
            continue
        else:
            print('O programa foi encerrado!')
            break