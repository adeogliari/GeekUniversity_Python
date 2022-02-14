"""
Fazer um programa para ler 5 valores, e em seguida, mostrar todos os valores lidos juntamente com o
maior, o menor e a média dos valores
"""

valores = []

for i in range(5):
    valores.append(int(input('Digite um valor: \n')))

print(f'Os valores digitador foram:')
print(*valores, sep=", ")
print(f'O maior valor digitado foi: \n'
      f'{max(valores)} \n'
      f'O menor valor digitado foi: \n'
      f'{min(valores)} \n'
      f'A média dos valores digitados é: \n'
      f'{sum(valores) / len(valores)}')