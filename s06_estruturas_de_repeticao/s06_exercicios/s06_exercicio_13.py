"""
13) Faça um programa que leia um número inteiro positivo par N e imprima
todos os números pares de 0 até N em ordem crescente.
"""

n = int(input('Digite um número par \n'))

if n % 2 == 0:
    for i in range(0, n + 1):
        if i % 2 == 0:
            print(i)
else:
    print('Número inválido')
