"""
9) Faça um programa que leia um número inteiro N e depois imprima
os N primeiros números naturais ímpares
"""

while_for = int(input('Digite 1 para usar WHILE e 2 para usar FOR \n'))

if while_for == 1 or while_for == 2:
    if while_for == 1:
        n = int(input('Digite um número inteiro \n'))
        count = 0
        number = 0

        while count != n:
            if number % 2 == 1:
                count += 1
                print(number)
            number += 1
    else:
        n = int(input('Digite um número inteiro \n'))
        count = 0
        for i in range(0, n*n):
            if i % 2 == 1:
                print(i)
                count += 1

            if count >= n:
                break
else:
    print('Opção inválida')