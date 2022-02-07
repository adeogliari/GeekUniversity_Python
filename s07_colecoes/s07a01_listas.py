"""
Listas

Listas em Python funcionam como vetores/matrizes (arrays em outras linguagens),
com a diferença de serem dinâmicos e também de podermos colocar qualquer tipo de dado.

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo:
    Ou seja, nestas linguagens se criar um array do tipo INT e com tamanho 5,
    este array SEMPRE será do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.

Já em Python:

    - Dinâmico: Não possuem tamanho fixo, ou seja, podemos criar a lista e
    simplesmente ir
    adicionando elementos (enquanto houver memória disponível);

    - Qualquer tipo de dado: Não possuem tipo de dado fixo, ou seja, podemos colocar
    qualquer tipo de dado;
    lista = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 45345345345]

As listas em Python são representadas por colchetes "[]"


---------------------------------------------------------------------------------


# Podemos facilmente checar se determinado valor está contido na lista
    num = 10
    if num in lista4:
        print(f'Encontrei o número {num}')
    else:
        print(f'Não encontrei o número {num}')


# Podemos facilmente ordenar uma lista
    lista1.sort()
    print(lista1)


# Podemos facilmente contar o número de ocorrências de um valor em uma lista
    print(lista1.count(1))
    print(lista5.count('e'))


# Para adicionar elementos em listas, utilizamos a função append
    print(lista1)
    lista1.append(42)
    print(lista1)

    # OBS: Com append, nós só conseguimos adicionar 1 elemento por vez
    # lista1.append(42, 55) = #ERRO
    lista1.append([8, 3, 1])
    print(lista1)


# Para buscar um elemento em uma lista
    if [8, 3, 1] in lista1:
        print('Encontrei a lista')
    else:
        print('Não encontrei a lista')


# Para adicionar vários elementos (1 a 1) diretamente na lista, usamos a função extend
    lista1.extend([123, '44', 67])
    print(lista1)


# Podemos inserir um novo elemento na lista informando a posição do índice
    # OBS: Isso não substitui o valor inicial, o mesmo será deslocado para a direita na lista
    lista1.insert(2, 'Novo Valor')
    print(lista1)


# Podemos facilmente juntar 2 listas
    lista1.extend(lista2)
    lista1 = lista1 + lista2
    print(lista1)


# Podemos facilmente inverter uma lista
    # Forma 1
        # lista1.reverse()
        # lista2.reverse()


    #Forma 2
        # print(lista1[::-1])
        # print(lista2[::-1])

# Podemos copiar uma lista
    lista6 = lista2.copy()
    print(lista6)


# Podemos contar quantos elementos existem dentro da lista
    print(len(lista5))


# Podemos remover facilmente o último elemento de uma lista
    # OBS: O pop não somente remove o último elemento, como também o retorna
    print(lista5)
    print(lista5.pop())
    lista5.pop()
    print(lista5)


# Podemos remover um elemento pelo índice
    # OBS: Os elementos a direita deste índice serão deslocados para a esquerda
    # OBS: Se não houver elemento no índice informado, teremos o erro IndexError.
    lista5.pop(2)
    print(lista5)


# Podemos remover todos os elementos (zerar a lista)
    print(lista5)
    lista5.clear()
    print(lista5)


# Podemos facilmente repetir elementos em uma lista
    nova = [1, 2, 3]
    print(nova)
    nova = nova * 3
    print(nova)


# Podemos converter uma string em uma lista
    # Exemplo 1
        curso = 'Programação em Python: Essencial'
        curso = curso.split()
        print(curso)
        # OBS: Por padrão, o split separa os elementos da lista pelo espaço entre eles
    # Exemplo 2
        curso = 'Programação,em,Python:,Essencial'
        curso = curso.split(',')
        print(curso)



# Convertendo uma lista em string
    Abaixo estamos falando: Pega a lista6, coloca espaço entre cada elemento e transforma
    em uma string
        curso = ' '.join(lista6)
        print(curso)


# Iterando sobre listas
    #Exemplo 1 - Utilizando for
        for elemento in lista1:
            print(elemento)

        # Soma de inteiros
            soma = 0
            for elemento in lista4:
                print(elemento)
                soma = soma + elemento
            print(soma)

        # Soma de string
            soma_string = ''
            for elemento in lista2:
                print(elemento)
                soma_string = soma_string + elemento
            print(soma_string)


    # Exemplo 2 - Utilizando while
        carrinho = []
        produto = ''
        while produto != 'sair':
            produto = input('Adicione um produto na lista ou digite "sair" para sair: \n')
            if produto != 'sair':
                carrinho.append(produto)

        for produto in carrinho:
            print(produto)


# Utilizando variáveis em listas
    numeros = [1, 2, 3, 4, 5]
    print(numeros)

    n1 = 1
    n2 = 2
    n3 = 3
    n4 = 4
    n5 = 5

    numeros = [n1, n2, n3, n4, n5]
    print(numeros)


# Fazemos acesso aos elementos de forma indexada
    cores = ['verde', 'amarelo', 'azul', 'branco']

    print(cores[0]) # verde
    print(cores[1]) # amarelo
    print(cores[2]) # azul
    print(cores[3]) # branco


# Fazemos acesso aos elementos de forma indexada inversa, (imagine como um circulo)
         -4         -3       -2       -1          0           1         2       3
    # ['verde', 'amarelo', 'azul', 'branco'] <- ['verde', 'amarelo', 'azul', 'branco']
    cores = ['verde', 'amarelo', 'azul', 'branco']

    print(cores[-1]) #branco
    print(cores[-2]) #azul
    print(cores[-3]) #amarelo
    print(cores[-4]) #verde

    for cor in cores:
        print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1


# Gerar indice em um for
    for indice, cor in enumerate(cores):
        print(indice, cor)


# Encontrar o índice de um elemento na lista
    numeros = [5, 6, 7, 5, 8, 9, 10]

    print(numeros.index(5)) # Em qual índice está o valor 5?
    # OBS: Retorna o índice do primeiro elemento encontrado

    # Podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar
    print(numeros.index(5, 1)) # Buscando a partir do indice 1

    # Podemos fazer busca dentro de um range, início/fim
    print(numeros.index(8, 3, 6))


# Revisão de slicing
    # lista[inicio:fim:passo]
    # range(inicio:fim:passo)

    lista = [1, 2, 3, 4, 5, 6]

    print(lista[1:]) # Começa no índice 0 e pega todos os elementos
    print(lista[2:5]) # Começa no índice 2 e pega até o indice 5 - 1
    print(lista[::2]) # Começa no índice 0 e pega todos os elementos de 2 em 2


# Invertendo valores em uma lista
nomes = ['Geek', 'University']

nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

nomes = ['Geek', 'University']
nomes.reverse()
print(nomes)


# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho
    # * Se os valores forem todos inteiros ou reais

    lista = [ 1, 2, 3, 4, 5, 6]

    print(sum(lista)) # soma
    print(max(lista)) # Máximo Valor
    print(min(lista)) # Mínimo Valor
    print(len(lista)) # Tamanho da lista


# Transformar uma lista em tupla
    lista = [1, 2, 3, 4, 5, 6]
    print(lista)
    print(type(lista))

    tupla = tuple(lista)
    print(tupla)
    print(type(tupla))


# Desempacotamento de listas
    lista = [1, 2, 3]

    num1, num2, num3 = lista

    print(num1)
    print(num2)
    print(num3)


# Copiando uma lista para outra (Shallow Copy e Deep Copy)
    # Forma 1 - Deep Copy
        lista = [1, 2, 3]
        print(lista)

        nova_lista = lista.copy()

        print(nova_lista)

        nova_lista.append(4)

        print(lista)
        print(nova_lista)

        OBS: Veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma
        nova lista, mas elas ficaram totalmente independentes, ou seja, modificando
        uma lista não afeta a outra. Isso em Python é chamado de Deep Copy.

    # Forma 2 - Shallow Copy

        lista = [1, 2, 3]
        print(lista)

        nova_lista = lista

        print(nova_lista)

        nova_lista.append(4)

        print(lista)
        print(nova_lista)

        OBS: Veja que utilizamos a cópia via atribuição e copiamos os dados da lista
        para a nova lista, mas após realizar modificação em uma das listas,
        essa modificação se refletiu em ambas as listas. Isso em Python é chamado de
        Shallow Copy.
"""

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

lista6 = ['Programação', 'em', 'Python:', 'Essencial']

cores = ['verde', 'amarelo', 'azul', 'branco']

