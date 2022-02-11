"""
3) Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado
das componentes deste vetor, armazenando o resultado em outro vetor. Os conjuntos têm
10 elementos cada. Imprimir todos os conjuntos.
"""

conjunto_a = []
conjunto_b = []

for valor in range(10):
    conjunto_a.append(int(input('Digite um valor: \n')))
    conjunto_b.append(conjunto_a[valor]**2)

print(conjunto_a)
print(conjunto_b)
