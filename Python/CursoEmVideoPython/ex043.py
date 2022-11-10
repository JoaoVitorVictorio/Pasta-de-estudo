# Analisando triângulos 2.0
from time import sleep
print('-='*20)
print('Analisador de triângulos')
print('-='*20)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
print('-='*20)

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima \033[32mPODEM FORMAR\033[m um triângulo', end=' ')
    if r1 == r2 and r2 == r3:
        print('\033[32mEQUILÁTERO!\033[m')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('\033[32mESCALENO!\033[m')
    else:
        print('\033[32mISÓSCELES!\033[m')
else:
    (print('Os segmentos acima \033[31mNÃO PODEM FORMAR\033[m um triângulo'))
