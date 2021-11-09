"""
8) Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e exiba na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota não possua um valor válido, este fato deve ser informado ao usuário e o programa termina.
"""

nota01 = float(input('Digite a primeira nota \n'))

if (nota01 < 0) or (nota01 > 10):
    print('Nota Inválida')
else:
    nota02 = float(input('Digite a segunda nota \n'))
    if (nota02 < 0) or (nota02 > 10):
        print('Nota inválida')
    else:
        print(f'A média entre as duas notas foi {(nota01 + nota02) / 2}')
