# Consumo na Gasolina e no Etanol
valorgasolina = float(input('Qual é o valor da gasolina? R$: '))
valoretanol = float(input('Qual é o valor do etanol: R$: '))
valortotalabastecido = float(input('Qual é o valor total que pretente abastecer? R$: '))
kmlgasolina = float(input('Quantos km seu veiculo faz com 1 litro de Gasolina?: '))
kmletanol = float(input('Quantos km seu veiculo faz com 1 litro de Etanol?: '))

litrosgasolina = valortotalabastecido/valorgasolina
litrosetanol = valortotalabastecido/valoretanol
kmg = litrosgasolina*kmlgasolina
kme = litrosetanol*kmletanol

print('-'*82)
print('\033[33mCaso seja abastecido com gasolina você terá o total de {:.2f} litro em seu tanque.\033[m\n'
      '\033[33mO seu veiculo irá rodar o total de {:.2f} km com este abastecimento na Gasolina\033[m'.format(litrosgasolina, kmg))
print('-'*82)
print('\033[32mCaso seja abastecido com etanol você terá o total de {:.2f} litros em seu tanque.\033[m\n'
      '\033[32mO seu veiculo irá rodar o total de {:.2f} km com este abastecimento na Etanol.\033[m'.format(litrosetanol, kme))
print('-'*82)
if kme <= kmg:
    print('\033[33mResultado: Neste caso compensa abastecer com GASOLINA!\033[m')
else:
    print('\033[32mResultado: Neste caso compensa abastecer com ETANOL!\033[m')
