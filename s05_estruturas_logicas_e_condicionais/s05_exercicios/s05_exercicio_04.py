"""
4) Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
    - O número digitado ao quadrado
    - A raiz quadrada ao número digitado
"""
import math

n1 = float(input('Digite um número \n'))

if n1 >= 0:
    print(f'O número {n1} ao quadrado é: {n1**2} \n'),
    print(f'A raiz quadrada do número {n1} é: {math.sqrt(n1)} \n')
else:
    print('Digite um número válido')
