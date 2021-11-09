"""
Ranges

- Precisamos conhecer o loop for para usar o ranges.
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória, mas sim de maneira especificada.

Formas gerais:

# Forma 01 range(valor_de_parada)
    for num in range(11):
        print(num)

OBS: valor_de_parada não inclusive (início padrão 0, e passo de 1 em 1)


# Forma 02 range(valor_de_inicio, valor_de_parada)
    for num in range(1, 11):
        print(num)

OBS: valor_de_parada não inclusive (início especificado pelo usuário, e passo de 1 em 1)


# Forma 03 range(valor_de_inicio, valor_de_parada, passo)
    for num in range (1, 10, 2):
        print(num)

OBS: valor_de_parada não inclusive (inicio especificado pelo usuário, e passo especificado pelo usuário)


# Forma 4 (inversa) range(valor_de_inicio, valor_de_parada, passo)
    for num in range(10, -1, -1)
        print(num)
"""