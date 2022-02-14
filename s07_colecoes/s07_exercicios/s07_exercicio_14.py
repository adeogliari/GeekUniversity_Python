"""
Faça um programa que leia um vetor de 10 posições e verifique se existem valores iguais e os
escreva na tela.
"""

from collections import Counter

vetor = []

for i in range(5):
    vetor.append(int(input('Digite um valor: \n')))

counter = Counter(vetor)
repetidos = []

for key, value in counter.items():
    if value > 1:
        repetidos.append(key)

print(f'Os valores repetidos são:')
print(*repetidos, sep=", ")
