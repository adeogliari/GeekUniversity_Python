"""
12) Leu um número inteiro. Se o número lido for negativo, escreva a mensagem 'Número inválido'. Se o número for positivo, calcular o logaritmo deste número.
"""
import math

n1 = int(input('Digite um número inteiro positivo: \n'))

if n1 < 0:
    print('Número inválido')
else:
    print(f'O logaritmo deste número é {math.log(n1)}')