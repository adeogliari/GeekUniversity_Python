"""
19) Escreva um algoritmo que leia um número inteiro entre 100 e 999
e imprima na saída cada um dos algarismos que compõem o número
"""

num = int(input('Digite um número entre 100 e 999 \n'))

while (num <= 100) or (num >= 999):
    num = int(input('Digite um número entre 100 e 999 \n'))

num = str(num)

for alg in num:
    print(alg)

