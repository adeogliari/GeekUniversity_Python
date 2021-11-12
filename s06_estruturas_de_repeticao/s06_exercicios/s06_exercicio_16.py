"""
16) Faça um programa que leia um número inteiro positivo impar N
imprima todos os núemros impares de 1 até N em ordem decrescente.
"""

n = int(input('Digite um número par \n'))

if n % 2 == 1:
    for i in range(n, -1, -1):
        if i % 2 == 1:
            print(i)
else:
    print('Número inválido')