"""
8) Escreva um programa que leia 10 números e escreva o menor
valor lido e o maior valor lido.
"""

tmp_maior = 0
tmp_menor = 0

for i in range(1, 11):
    num = int(input(f'Digite o número {i} de 10 a ser analisado \n'))

    if i == 1:
        tmp_maior = tmp_menor = num

    elif num > tmp_maior:
        tmp_maior = num

    elif num < tmp_menor:
        tmp_menor = num

print(f'O menor número digitado é {tmp_menor} e o maior número digital é {tmp_maior}')