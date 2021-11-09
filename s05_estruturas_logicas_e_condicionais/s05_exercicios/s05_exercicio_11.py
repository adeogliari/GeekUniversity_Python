"""
11) Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a soma de todos os seus algarismos. Por exemplo, ao número 251 corresponderá o valor 8 (2 + 5 + 1). Se o número lido não dor maior do que zero, programa terminará com a mensagem 'Número inválido'
"""

numero = int(input('Digite um número inteiro maior que zero: \n'))

if numero > 0:
    numero = str(numero)
    print(sum(int(i) for i in numero))
else:
    print('Número inválido')
