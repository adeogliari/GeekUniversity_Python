"""
4) Escreva um programa que declare um inteiro, incialize-o com 0, e incremente-o de 1000 em 1000, imprimindo seu valor na tela, até que seu valor seja 100000(cem mil).
"""

num = 0
for n in range(0, 100000 + 1000, 1000):
    num = n
    print(n)


num = 0
print(num)
while num < 100000:
    num += 1000
    print(num)
