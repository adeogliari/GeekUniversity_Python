"""
7) Escreva um programa que leia 10 números inteiros e os armazene em um vetor.
Imprima o vetor, o maior elemento e a posição que ele se encontra.
"""

vetor = []

for i in range(10):
    vetor.append(int(input('Digite um valor: \n')))

print(f'O vetor é: \n'
      f'{vetor} \n'
      f'O maior número do vetor é: \n'
      f'{max(vetor)} \n'
      f'A posição do maior número do vetor é: \n'
      f'{vetor.index(max(vetor))} \n\')