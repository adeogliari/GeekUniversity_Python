"""
1) Faça um programa que determine e mostre os cinco primeiros múltiplos de 3, considerando números maiores que 0
"""

contador = 0

for n in range(1, 1000):
    if (n % 3 == 0) and (contador <= 5):
        print(n)
        contador += 1
