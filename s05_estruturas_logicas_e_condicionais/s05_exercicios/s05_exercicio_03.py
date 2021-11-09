"""
3) Leia um número real. Se o número for positivo imprima a raiz quadrada. Do contrário, imprima o número ao quadrado.
"""
import math

n1 = float(input('Digite um número: \n'))

if n1 > 0:
    print(f'A raiz quadrada de {n1} é {math.sqrt(n1)}')
elif n1 == 0:
    print('Você digitou o número 0')
else:
    print(f'{n1} ao quadrado é {n1**2}')
