"""
18) Faça um programa que mostre ao usuário um menu com 4 opções de operações matemáticas(as básicas, por exemplo). O
suário escolhe uma das opções e o seu programa então pede dois valores numéricos e realiza a operação, mostrando o
resultado e saindo.
"""

opcao = int(input('Digite o número da opção desejada:'
                  '\n 1- Somar / 2- Subtrair '
                  '\n 3- Multiplicar / 4- Dividir \n'))

if opcao == 1:
    n1 = float(input('Digite a primeira parcela \n'))
    n2 = float(input('Digite a Segunda parcela \n'))
    print(f'A soma de {n1} e {n2} é {n1 + n2}')

elif opcao == 2:
    n1 = float(input('Digite o minuendo \n'))
    n2 = float(input('Digite o subtraendo \n'))
    print(f'O resto/diferença de {n1} e {n2} é {n1 - n2}')

elif opcao == 3:
    n1 = float(input('Digite o primeiro fator \n'))
    n2 = float(input('Digite o segundo fator \n'))
    print(f'O produto de {n1} e {n2} é {n1 * n2}')

elif opcao == 4:
    n1 = float(input('Digite o dividendo \n'))
    n2 = float(input('Digite o divisor \n'))
    print(f'O resultado da divisão entre {n1} e {n2} é {n1 / n2}')
else:
    print('Digite uma opção válida')
