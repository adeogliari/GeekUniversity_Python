"""
5) Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui.
"""

lista = []
pares = []
count = 0

for i in range(10):
    lista.append(int(input('Digite um valor: \n')))
    if lista[i] % 2 == 0:
        count += 1
        pares.append(lista[i])

print(f'A lista possui {count} valores pares: \n'
      f'{pares}')

