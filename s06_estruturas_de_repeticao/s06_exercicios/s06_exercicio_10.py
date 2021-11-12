"""
10) Faça um programa que calcule e mostre a soma dos 50
primeiros números pares.
"""

n = 50
soma = 0

for i in range(0, (n * 2) + 1):
    if i % 2 == 0:
        soma += i
print(soma)
