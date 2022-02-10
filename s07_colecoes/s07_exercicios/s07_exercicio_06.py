"""
6) Faça um programa que receba do usuáro um vetor com 10 posições.
Em sequida deverá ser impresso o maior e o menor elemento do vetor.
"""

vetor = []

for i in range(10):
    vetor.append(int(input('Digite um valor: \n')))
print(f'O menor valor do vetor é {min(vetor)} e o maior valor é {max(vetor)}')