# Contagem regressiva
from time import sleep

for num in range(10, -1, -1):
    sleep(1)
    print(num)
print('Chegamos ao fim da contagem!')
