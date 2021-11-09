"""
5) Faça um programa que peça ao usuário para digitar 10 valores e some-os.
"""

soma = 0
for n in range(10):
    num = float(input(f'Digite o valor {n + 1} de 10 para ser somado \n'))
    soma = soma + num
print(f'{soma}')
