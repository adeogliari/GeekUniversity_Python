"""
6) Escreva um programa que, dados dois números inteiro, mostre na tela o maior deles, assim como a diferença existentes entre ambos.
"""

n1, n2 = int(input('Digite o primeiro número: \n')), \
         int(input('Digite o segundo número: \n'))

if n1 > n2:
    print(f'O maior número é o {n1}, a diferença entre eles é {n1 - n2}')
elif n1 < n2:
    print(f'O maior número é o {n2}, a diferença entre eles é {n2 - n1}')
else:
    print('Os números digitados são iguais')
