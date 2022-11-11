# Um print especial
def escreva(txt):
    tam = len(txt) + 4
    print('=' * tam)
    print(f'  {txt}')
    print('=' * tam)

escreva('\033[31mJoão\033[m')
escreva('\033[32mVitor\033[m')
escreva('\033[33mVictorio\033[m')