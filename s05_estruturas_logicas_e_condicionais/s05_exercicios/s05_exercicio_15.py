"""
15) Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. Isto é, domingo se 1, segunda-feira se 2, e assim por diante.
"""

dia = int(input('Digite o dia da semana, sendo 1 para domingo e 7 para sábado \n'))

if dia == 1:
    print('Hoje é Domingo')
elif dia == 2:
    print('hoje é Segunda-Feira')
elif dia == 3:
    print('Hoje é Terça-Feira')
elif dia == 4:
    print('Hoje é Quarta-Feira')
elif dia == 5:
    print('Hoje é Quinta-Feira')
elif dia == 6:
    print('Hoje é Sexta Feira')
elif dia == 7:
    print('Hoje é sábado')
else:
    print('Dia Inválido')
