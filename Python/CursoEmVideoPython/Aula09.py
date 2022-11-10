#Fatiamento
'''frase = 'Aprendendo Python'
print(frase[3])
print(frase[3:13])
print(frase[:10])
print(frase[11:])
print(frase[11:13])
print(frase[1:5:13])
print(frase[5::3])'''

#Analise (Conta as letras)
'''frase = 'Aprendendo Python'
print(len(frase))'''

#Count (conta a quantidade de letras escolhidas)
'''frase = 'Aprendendo Python'
print(frase.count('o', 0, 13))'''

#Find (Indica em qual posição começou as letras entre parenteses)
'''frase = 'Aprendendo Python'
print(frase.find('den'))'''

#Função IN (mostra se existe a palavra dentro da frase) e find (mostra a posição palavra dentro da frase)
'''frase = 'Aprendendo Python'
print('Python' in frase)
print(frase.find('Python'))'''

#Transformação (Trocar, reposisionar, substituir por outra palavra)
'''frase = 'Aprendendo Python'
print(frase.replace('Python','Android'))'''

#Segundo método de print replace
'''frase = 'Aprendendo Python'
frase = frase.replace('Python','Android)'
print(frase)'''

#Upper (Deixar letras em maiúsculo)
'''frase = 'Aprendendo Python'
print(frase.upper())'''

#Lower (Deixar letras em minusculas)
'''frase = 'Aprendendo Python'
print(frase.lower())'''

#Capitalize (Deixa só o primeiro caracter em maiúsculo)
'''frase = 'Aprendendo Python'
print(frase.capitalize())'''

#Title (Deixa palavra por palavra com o primeiro caracter em maiúsculo)
'''frase = 'Aprendendo Python'
print(frase.title())'''

#Strip (Remove o espaço do começo ou do fim, mas matem os do meio)
'''frase = '   Aprendendo Python  '
print(frase.strip())'''

#Rstrip (Remove o espaço somente do fim da frase)
'''frase = 'Aprendendo Python      '
print(frase.rstrip())'''

#Lstrip (Remove o espaço somente do inicio da frase)
'''frase = '                 Aprendendo Python'
print(frase.lstrip())'''

#Split (Cria uma divisão em cada palavra da frase, dentro de listas diferentes)
'''frase = 'Aprendendo Python'
print(frase.split())'''

#Segundo método
'''frase = 'Aprendendo Python'
dividido = frase.split()
print(dividido[0])'''

#Join (Separa cada letra das palavras por separador -)
'''frase = 'Aprendendo Python'
print('-'.join(frase))'''













