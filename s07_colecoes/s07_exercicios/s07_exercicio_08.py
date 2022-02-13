"""
8) Crie um programa que lê 6 valores inteiros e, em seguida, mostre
na tela os valores lidos na ordem inversa
"""

vetor = []

for i in range(6):
    vetor.append(int(input('Digite um valor: \n')))

vetor_cp = vetor.copy()
vetor_cp.reverse()

print(f'O vetor na ordem inversa é: \n'
      f'{vetor[::-1]}')

print(f'O vetor na ordem inversa é: \n'
      f'{vetor_cp}')