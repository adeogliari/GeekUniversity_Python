"""
19) Faça um programa para verificar se um determinado número inteiro é divisível por 3 ou 5, mas não simultaneamente
pelos dois.
"""

numero = int(input('Digite um número para verificar se é divisível por 3 ou 5 mas não pelos dois simultaneamente \n'))

if (numero % 5 == 0) and (numero % 3 == 0):
    print(f'O número {numero} é divisível por 3 e 5 simultaneamente')

elif numero % 3 == 0:
    print(f'O número {numero} é divisível por 3')

elif numero % 5 == 0:
    print(f'O número {numero} é divisível por 5 \n')

else:
    print(f'O número {numero} não atende a nenhum dos requisitos')
