"""
Fazer um programa para ler 5 valores e, em seguida, mostrar a posição onde se encontram o maior e o
menor valor.
"""

valores = []

for i in range(5):
    valores.append(int(input('Digite um valor: \n')))

print(f'O maior valor está na posição {valores.index(max(valores))} e o menor valor se encontra '
      f'na posição {valores.index(min(valores))}')