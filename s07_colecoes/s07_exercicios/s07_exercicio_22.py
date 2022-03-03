"""
Faça um programa que leia dois vetores de 10 posições e calcule outro vetor contendo nas
posições pares os valores do primeiro e nas posições impares os valores do segundo.
"""

vetor_a = []
vetor_b = []
vetor_c = []

for i in range(10):
    vetor_a.append(int(input('Digite um valor para inserir no vetor A: \n')))

for i in range(10):
    vetor_b.append(int(input('Digite um valor para inserir no vetor B: \n')))

for i in range((len(vetor_a) + len(vetor_b))):
    print(i)

print(vetor_c)


