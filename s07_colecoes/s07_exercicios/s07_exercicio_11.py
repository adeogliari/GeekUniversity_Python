"""
Faça um programa que preencha um vetor com 10 números reais, calcule e mostre a quantidade de
números negativos e a soma dos números positivos desse vetor:
"""

vetor = []
vetor_negativo = []
vetor_positivo = []

for i in range(10):
    vetor.append(float(input('Digite um valor positivo ou negativo: \n')))

for i in vetor:
    if i < 0:
        vetor_negativo.append(i)
    else:
        vetor_positivo.append(i)

print(f'A quantidade de números negativos digitados é {len(vetor_negativo)} \n'
      f'A soma dos números positivos digitados é {sum(vetor_positivo)}')

print()

print(f'{vetor} \n {vetor_positivo} \n {vetor_negativo}')
