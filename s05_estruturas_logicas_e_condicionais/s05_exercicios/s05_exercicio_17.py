"""
17) Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que: A = ((basemaior + basemenor) * altura)
/ Lembre-se a base maior e a base menor devem ser números maiores que zero.
"""

base_maior = float(input('Digite o tamanho da base maior do trapézio em metros: \n'))

if base_maior > 0:
    base_menor = float(input('Digite o tamanho da base menor do trapézio em metros: \n'))

    if base_menor > 0:
        altura = float(input('Digite a altura do trapézio em metros: \n'))

        if altura > 0:
            print(f'O tamanho da área do trapézio é de {(base_maior * base_menor) * altura} metros')

        else:
            print('Valor inválido')
    else:
        print('Valor inválido')
else:
    print('Valor inválido')

