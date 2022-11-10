# Exercício de criar um programa para saber a distância correspondente em metros.
n1 = float(input('Uma distância em metros: '))
km = n1 / 1000
hm = n1 / 100
dam = n1 / 10
dm = n1 * 10
cm = n1 * 100
mm = n1 * 1000
print('A medida de {}m, corresponde a:\n{} km\n{} hm\n{} dam\n{:.0f} dm\n{:.0f} cm\n{:.0f} mm.'.format(n1,km,hm,dam,dm,cm,mm))








