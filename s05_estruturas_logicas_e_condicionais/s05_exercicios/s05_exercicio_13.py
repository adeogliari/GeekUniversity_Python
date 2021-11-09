"""
13) Faça um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e a segunda prova têm peso 1 e a terceira tem peso 2. Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 60 pontos.
"""

nota_prova01 = float(input('Digite a nota da prova 01 \n'))

if (nota_prova01 >= 0) and (nota_prova01 <= 100):
    nota_prova02 = float(input('Digite a nota da prova 02 \n'))

    if (nota_prova02 >= 0) and (nota_prova02 <= 100):
        nota_prova03 = float(input('Digite a nota da prova 03 \n'))

        if (nota_prova03 >= 0) and (nota_prova03 <= 100):
            media_ponderada = ((nota_prova01 + nota_prova02) + (2 * nota_prova03))/4

            if media_ponderada > 60:
                print(f'O aluno foi aprovado e sua média ponderada foi: {media_ponderada} \n')

            else:
                print(f'O Aluno foi reprovado e sua média ponderada foi: {media_ponderada} \n')

        else:
            print('Nota inválida')
    else:
        print('Nota inválida')
else:
    print('Nota inválida')


