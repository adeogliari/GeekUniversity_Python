"""
Escreva um programa que leia números inteiros no intervalo [0, 50] e os armazene em um vetor com
10 posições. Preencha um segundo vetor apenas com os números ímpares do primeiro vetor. Imprima
os dois vetores, 2 elementos por linha
"""

vetor = []
impares_vetor = []

for i in range(10):
    numero = int(input('Digite um número entre 0 e 50: \n'))
    while (numero < 0) or (numero > 50):
        numero = int(input('Digite um número entre 0 e 50: \n'))
    vetor.append(numero)

for key, value in enumerate(vetor):
    if value % 2 != 0:
        impares_vetor.append(value)


for i in range(0, len(vetor), 2):
    print(f'{vetor[i]}', end='')

    if len(vetor) > i + 1:
        print(vetor[i + 1])
