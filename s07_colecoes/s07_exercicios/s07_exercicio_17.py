"""
Leia um vetor de 10 posições e atribua valor 0 para todos os elementos que possuírem valores
negativos.
"""

vetor = []

for i in range(10):
    vetor.append(int(input('Digite um valor: \n')))

for key, value in enumerate(vetor):
    if value < 0:
        vetor[key] = 0

print(vetor)
