"""
Leia um vetor com 20 números inteiros. Escreva os elementos do vetor eliminando elementos repetidos.
"""

from collections import Counter

vetor = []

for i in range(20):
    vetor.append(int(input('Digite um valor inteiro: \n')))

counter_vetor = Counter(vetor)
numeros_n_repetidos = []

for key, value in counter_vetor.items():
    if value == 1:
        numeros_n_repetidos.append(key)

print(f'Os números não repetidos do vetor são: \n')
print(*numeros_n_repetidos, sep=", ")


