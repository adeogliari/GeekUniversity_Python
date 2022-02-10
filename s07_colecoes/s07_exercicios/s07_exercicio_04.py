"""
4) Faça um programa que leia um vetor de 8 posições e, em seguida,
leia também dois valores X e Y quaisquer correspondentes a duas posições
no vetor. Ao final seu programa deverá escrever a soma dos valores encontrados
nas respectivas posições X e Y.
"""

vetor = []
for i in range(8):
    vetor.append(int(input('Digite um valor valor para o vetor: \n')))
print(vetor)

posicao = []
for i in range(2):
    posicao.append(int(input('Digite uma posição do vetor: \n')))

soma = vetor[posicao[0]] + vetor[posicao[1]]
print(f'A soma dos valores encontrados nas posições {posicao[0]} e {posicao[1]} do vetor {vetor} é:'
      f' {soma}')