s = c = n = 0
while True:
    n = int(input('Digite um valor (999 faz o programa parar): '))
    if n == 999:
        break
    c += 1
    s += n
print(f'A soma dos {c} valores é: {s}!')