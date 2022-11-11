# Lista ordenada sem repetições
lista = []
for c in range(0, 5):
    num = int(input('Digite um número: '))
    if c == 0:
        lista.append(num)
        print('Adicionado ao final da lista...')
    elif num > lista[len(lista)-1]:
        lista.append(num)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos +=1
print('=*' * 27)
print(f'Os números digitados em ordem foram: {lista}')

