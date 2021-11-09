"""
7) Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem 'Números iguais'.
"""

n1, n2 = float(input('Digite o primeiro número \n')), \
         float(input('Digite o segundo número \n'))

if n1 < n2:
    print(f'{n2}')
elif n1 == n2:
    print(f'Os números são iguais')
else:
    print(f'{n1}')