"""
Faça um programa que leia dois vetores de 10 posições e calcule outro vetor contendo nas
posições pares os valores do primeiro e nas posições impares os valores do segundo.
"""

vetor_a = []
vetor_b = []
vetor_c = []

for i in range(10):
    vetor_a.append(float(i))
    vetor_b.append(int(i))
    # vetor_a.append(int(input('Digite um valor para inserir no vetor A: \n')))

print(vetor_a)
print(vetor_b)

counter_par = 0
counter_impar = 0

for i in range(len(vetor_a + vetor_b)):
    if i % 2 == 0:
        vetor_c.append(vetor_a[counter_par])
        counter_par += 1
    else:
        vetor_c.append(vetor_b[counter_impar])
        counter_impar += 1


print(vetor_c)


