"""
Faça um programa que leia um vetor de 10 números. Leia o número x. Conte os múltiplos de um
número inteiro x num vetor e mostre-os na tela.
"""

vetor = []
multiplos = []

for i in range(10):
    vetor.append(int(input('Digite um número para colocar no vetor: \n')))

numero = int(input('Digite um número: \n'))

for key, value in enumerate(vetor):
    if value % numero == 0:
        multiplos.append(value)

print(f'Os números múltiplos de {numero} que estão no vetor são:')
print(*multiplos, sep=", ")
