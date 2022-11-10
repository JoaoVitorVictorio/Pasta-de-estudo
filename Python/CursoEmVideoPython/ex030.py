# Radar eletrônico
v = int(input('Qual é a velocidade atual do carro? '))
m = (v - 80) * 7
if v <= 80:
    print('\033[36mTenha um bom dia! Dirija com segurança!\033[m')
else:
    print('\033[31mMULTADO!\033[m Você excedeu o limite permitido que é de 80km/h')
    print('Você deve pagar uma multa de \033[31mR${:.2f}\033[m'.format(m))
    print('\033[36mTenha um bom dia! Dirija com segurança!\033[m')
