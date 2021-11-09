"""
7) Faça um programa que leia 10 inteiros positivos, ignorando não positivos,
e imprima sua média
"""

media = 0

for n in range(1, 11):
    num = int(input(f'Digite o valor {n} de 10 \n '))
    if num >= 0:
        media += num
    if n == 10:
        print(f'A média dos números digitados é {media/n}')
