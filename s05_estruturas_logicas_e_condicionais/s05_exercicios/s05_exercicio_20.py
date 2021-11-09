"""
20) Dados três valores A, B, C, verificar se eles podem ser valores dos lados  de um triângulo e, se forem,
se é um triângulo escaleno, equilátero ou isóscele, considerando os seguintes conceitos:
    - O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados.
    - Chama-se equilátero o triângulo que tem três lados iguais
    - Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
    - Recebe o nome de escaleno o triângulo que tem os três lados diferentes.
"""

lado_a = float(input('Digite o tamanho do lado A \n'))
lado_b = float(input('Digite o tamanho do lado B \n'))
lado_c = float(input('Digite o tamanho do lado C \n'))

if (lado_a < (lado_b + lado_c)) \
        and (lado_b < (lado_a + lado_c)) \
        and (lado_c < (lado_a + lado_b)):

    if (lado_a == lado_b) and (lado_a == lado_c):
        print('Triângulo Equilátero')

    elif ((lado_a == lado_b) and (lado_a != lado_c)) \
            or ((lado_b == lado_c) and (lado_b != lado_a)) \
            or ((lado_c == lado_a) and (lado_c != lado_b)):
        print('Triângulo Isósceles')

    elif lado_a != lado_b != lado_c:
        print('Triângulo Escaleno')

else:
    print('Não é um triângulo')
