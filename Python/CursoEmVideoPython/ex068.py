# Tabuada v3.0
c = n = 0
while True:
    n = int(input('Quer vizualizar a tabuada de qual número? '))
    c += 1
    print('-' * 45)
    if n < 0:
        break
    for c in range (1, 11):
        print(f'{n} x {c:2} = {n * c}')
    print('-' * 45)
print('Programa finalizado!')



