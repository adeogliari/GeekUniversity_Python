"""
10) Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando as seguintes fórmulas (onde h corresponde à altura):
    - Homens: (72.7 * h) - 58
    - Mulheres: (62.1 * h) - 58
"""

altura = float(input('Digite sua altura em metros usando ponto no lugar da vírgula \n'))

if altura < 0.5 or altura > 2.5:
    print('altura inválida')
else:
    sexo = int(input('Se você for homem digite 1, se for mulher digite 2 \n'))
    if sexo == 1:
        print(f'Você é homem e seu peso ideal é {(72.7 * altura) - 58}kg')
    elif sexo == 2:
        print(f'Você é mulher e seu peso ideal é {(62.1 * altura) - 58}kg')
    else:
        print('Opção inválida')
