"""
14) A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo de 0 até 10, respectivamente, a trabalho do laboratório, a uma avaliação semestral e a um exame final. A média das três notas mencionada anteriormente obedece aos pesos: Trabalho de Laboratório: 2; Avaliações Semestral: 3; Exame final: 5. De acordo com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2.9), de recuperação (entre 3 e 4.9) ou se foi aprovado. Faça todas as verificações necessárias.
"""

nota_lab = float(input('Digite a nota do Trabalho de Laboratório \n'))

if (nota_lab >= 0) and (nota_lab <= 10):
    nota_avaliacao = float(input('Digite a nota da Avaliação Semestral \n'))

    if (nota_avaliacao >= 0) and (nota_avaliacao <= 10):
        nota_exame = float(input('Digite a nota do Exame Final \n'))

        if (nota_exame >= 0) and (nota_exame <= 10):
            media = (((nota_lab * 2)
                     + (nota_avaliacao * 3)
                     + (nota_exame * 5))
                     / (2 + 3 + 5)
                     )
            if media <= 2.9:
                print(f'A média foi de {media} e o aluno está reprovado')

            elif (media > 2.9) and (media <= 4.9):
                print(f'A média foi de {media} e o aluno está em recuperação')

            else:
                print(f'A média foi de {media} e o aluno está aprovado')

        else:
            print('Nota inválida')
    else:
        print('Nota inválida')
else:
    print('Nota inválida')

