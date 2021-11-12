"""
18) Escreva um algoritmo que leia certa quantidade de números
e imprima o maior deles e quantas vezes o maior número foi lido.
A quantidade de números a serem lidos deve ser fornecida pelo usuário.
"""

quantidade_numeros = int(input('Digite a quantidade de números a serem lidos \n'))
maior = 0
count = 0

for _ in range(quantidade_numeros):
    num = int(input(f'Digite o um número: \n'))

    if num > maior:
        maior = num
        count = 0
    else:
        count += 1

print(f'O maior número digitado foi {maior} e ele foi lido {count} vezes')
