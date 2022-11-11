# Indice de massa corporal
peso = float(input('Qual é o seu peso (Kg)? '))
altura = float(input('Qual é a sua altura (m)? '))
imc = peso / (altura ** 2)

print('O seu IMC é de: {:.1f}'.format(imc))

if imc < 18.5:
    print(('Você ABAIXO DO PESO ideal'))
elif imc >= 18.5 and imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif imc > 25 and imc < 30:
    print('Você está SOBREPESO!')
elif imc > 30 and imc < 40:
    print('Você está em OBESIDADE, cuidado com sua saúde e consulte um médico!')
else:
    print('CUIDADO!, você está com OBESIDADE MÓRBIDA, consulte um médico e cuide da tua saúde!')
