"""
Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule e imprima a
média geral.
"""

nota = []

for i in range(1, 16):
    nota.append(int(input(f'Digite a nota do aluno {i}: \n')))

print(f'A média geral dos alunos foi {sum(nota) / len(nota)}')
