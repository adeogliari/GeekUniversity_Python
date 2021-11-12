"""
17) Faça um programa que leia um número inteiro positivo
n e calcule a soma dos n primeiros números naturais.
"""

n = int(input('Digite um número inteiro positivo \n'))
soma = 0

for i in range(0, n + 1):
    soma += i
print(soma)
