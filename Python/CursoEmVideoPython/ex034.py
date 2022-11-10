# Maior e menor valor
pv = int(input('Primeiro valor: '))
sv = int(input('Segundo valor: '))
tv = int(input('Terceiro valor: '))
# Verificando quem é menor
if pv < sv and pv < tv:
    menor = pv
if sv < pv and sv < tv:
    menor = sv
if tv < pv and tv < pv:
    menor = tv
# Verificando quem é maior
if pv > sv and pv > tv:
    maior = pv
if sv > pv and sv > tv:
    maior = sv
if tv > pv and tv > sv:
    maior = tv
print('O MENOR valor digitado foi: {}'.format(menor))
print('O MAIOR valor digitado foi: {}'.format(maior))
