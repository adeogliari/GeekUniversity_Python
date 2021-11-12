"""
20) Ler uma sequência de números inteiros e determinar se eles são pares
ou não. Deverá ser informado o número de dados lidos e números de valores
pares. O processo termina quando for digitado o número 1000.
"""

num, count_num, count_pares = (0, 0, 0)

for i in range(1000):
    num = int(input('Digite um número \n'))

    if num < 0:
        num = int(input('Digite um número positivo \n'))

    count_num += 1

    if num % 2 == 0:
        count_pares += 1

print(f'O número de dados lidos foi de {count_num} e possui {count_pares} números pares')
