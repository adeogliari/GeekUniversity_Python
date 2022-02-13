"""
8) Crie um programa que lê 6 valores inteiros pares e, em seguida, mostre
na tela os valores lidos na ordem inversa
"""

pares = []

while len(pares) < 6:
    number = int(input('Digite um número: \n'))
    if number % 2 == 0:
        pares.append(number)

pares_cp = pares.copy()
pares.reverse()

print(f'Os número pares em ordem inversa da digitada são: \n'
      f'{pares_cp[::-1]}')

print(f'Os número pares em ordem inversa da digitada são: \n'
      f'{pares}')
