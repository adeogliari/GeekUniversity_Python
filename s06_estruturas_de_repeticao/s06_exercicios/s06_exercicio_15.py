"""
15) Faça um programa que leia um número inteiro positivo impar N e imprima
todos os números impares de 1 até N em ordem crescente.
"""

n = int(input('Digite um número ímpar \n'))

if n % 2 == 1:
    for i in range(0, n + 1):
        if i % 2 == 1:
            print(i)
else:
    print('Número inválido')
