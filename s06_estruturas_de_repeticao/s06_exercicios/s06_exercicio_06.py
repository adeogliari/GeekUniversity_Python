"""
6) Faça um programa que leia 10 inteiros e imprima sua média.
"""

media = 0

for n in range(1, 11):
    num = float(input(f'Digite o valor {n} de 10 para ser somado \n'))
    media += num
    if n == 10:
        print(f'{media/n}')
