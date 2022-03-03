"""
Faça um programa que receba do usuário dois vetores, A e B, com 10 números inteiros cada.
Crie um novo vetor denominado C calculando C = A - B. Mostre na tela os dados do vetor C
"""

# Lista
vetor_a = []
vetor_b = []
vetor_c = []

for i in range(10):
    vetor_a.append(int(input('Digite um valor para inserir no vetor A: \n')))

print(f'Vetor A: {vetor_a}')

for i in range(10):
    vetor_b.append(int(input('Digite um valor para inserir no vetor B: \n')))

print(f'Vetor B: {vetor_b}')

for i in vetor_a:
    if i not in vetor_b:
        vetor_c.append(i)

print(f'Vetor C: {vetor_c}')



# Conjunto
conjunto_a = set()
conjunto_b = set()
conjunto_c = set()

for i in range(10):
    conjunto_a.add(int(input('Digite um valor para inserir no vetor A: \n')))

print(f'Conjunto A: {conjunto_a}')

for i in range(10):
    conjunto_b.add(int(input('Digite um valor para inserir no vetor B: \n')))

print(f'Conjunto C: {conjunto_b}')

conjunto_c = conjunto_a.difference(conjunto_b)

print(f'Conjunto C: {conjunto_c}')