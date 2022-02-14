"""
Faça um programa que leia um vetor de 5 posições para números reais e, depois, um código inteiro.
Se o código for zero, finalize o programa; se for 1, mostre o vetor na ordem direto; se for 2,
mostre o vetor na ordem inversa. Caso o código for diferente de 1 e 2, escreva uma mensagem
informando que o código é inválido.
"""

vetor = []

for i in range(5):
    vetor.append(int(input('Digite um valor: \n')))

codigo = int(input('Digite: \n'
                   '0 - Sair \n'
                   '1 - Mostrar vetor na ordem direta \n'
                   '2 - Mostrar o vetor na ordem inversa \n'))

while (codigo != 0) and (codigo != 1) and (codigo != 2):
    codigo = int(input('Código Inválido, Digite: \n'
                       '0 - Sair \n'
                       '1 - Mostrar vetor na ordem direta \n'
                       '2 - Mostrar o vetor na ordem inversa \n'))

if codigo == 0:
    print('Programa encerrado')
elif codigo == 1:
    print(f'{vetor}')
else:
    print(f'{vetor[::-1]}')
