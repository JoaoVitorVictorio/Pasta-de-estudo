# Tratamento de Erros e Exceções
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro: # Tipo de erro
    print(f'Problema encontrado: {erro.__class__}')
except (ValueError, TypeError):
    print('Problema encontrado no tipo de dado digitado')
except ZeroDivisionError:
    print('Não é possivel dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally: # Finaliza com uma mensagem
    print('Programa finalizado.')

