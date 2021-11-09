"""
2) Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.
"""
import math

n1 = float(input('Digite um número \n'))

if n1 > 0:
    print(f'A raiz quadrada de {n1} é {math.sqrt(n1)}')
elif n1 == 0:
    print('Você digitou o número 0')
else:
    print('O número informado é inválido')
