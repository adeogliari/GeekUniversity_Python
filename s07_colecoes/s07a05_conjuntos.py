"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência à Teoria
dos Conjuntos da Matemática.

- Aqui no Python, os conjuntos são chamados de Sets.

Dito isto, da mesma forma que na matemática:

- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não sáo indexados;

Conjutnso são bons para se utilizar quando precisamos armazenar elementos mas não nos
importamos com a ordenação deles. Quando não precisamos nos preocupar com chaves,
valores e itens duplicados.

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre Conjutnos (Set) e Mapas (Dicionários) em Python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;


# Definindo um conjunto:
    OBS: Ao criar um conjunto, caso seja adicionar um valor já existente, o mesmo será
    ignorado sem gerar erro e não fará parte do conjunto.
    # Forma 1
        s = set({1, 2, 3, 4, 5, 6, 7, 2, 3}) # Repare que temos valores repetidos
        print(s)
        print(type(s))

    # Forma 2
        s = {1, 2, 3, 4, 5, 5}
        print(s)
        print(type(s))


# Podemos vefiricar se determinado elemento está contido no conjunto
    if 3 in s:
        print('Tem o 3')
    else:
        print('Não tem o 3')


# Importante lembrar que, além de não termos valores duplicados, não temos ordem
    dados = (99, 2, 34, 23, 2, 12, 1, 44, 5, 34)

    # Listas aceitam valores duplicados, então temos 10 elementos
        lista = list(dados)
        print(f'Lista: {lista} com {len(lista)} elementos')

    # tuplas aceitam valores duplicados, então temos 10 elementos
        tupla = tuple(dados)
        print(f'Tupla: {tupla} com {len(tupla)} elementos')

    # dicionarios não aceitam chaves duplicados, então temos 8 elementos
        dicionario = {}.fromkeys(dados, 'dict')
        print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')

    # conjuntos não aceitam valores duplicados, então temos 8 elementos
        set = set(dados)
        print(f'Set: {set} com {len(set)} elementos')


# Assim como todo outro conjunto Python podemos colocar tipos de dados misturados em Sets
    set = {1, 'b', True, 34.22, 44}
    print(set)
    print(type(set))

    for valor in set:
        print(valor)


# Usos interessantes com sets

    - Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu e
    os visitantes informam manualmente a cidade de onde vieram.

    -Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos
    adicionar novos elementos e ter repetição

        cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande',
                   'São Paulo', 'Cuiaba',]

        print(cidades)
        print(type(cidades))
        print(len(cidades))

        - Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos.
        - Podemos utilizar o set para isso:
            print(set(cidades))
            print(type(set(cidades)))
            print(len(set(cidades)))


# Adicionando elementos em um conjunto
    s = {1, 2, 3}
    s.add(4)
    print(s)


# Remover elementos em um conjunto
    # Forma 1
        s.remove(3) # NÃO é índice, informamos o valor a ser removido, se não encontrado dá erro
        print(s)

    # Forma 2
        s.discard(2) # Não gera erro quando o valor não for encontrado.
        print(s)


# Copiando um conjunto para outro.
    # Forma 1 - Deep Copy
        novo_conjunto = s.copy()
        print(novo_conjunto)

        novo_conjunto.add(4)

        print(s)
        print(novo_conjunto)

    # Forma 2 - Shallow Copy
        novo_conjunto = s
        print(novo_conjunto)

        novo_conjunto.add(4)

        print(s)
        print(novo_conjunto)


# Podemos remover todos os itens de um conjunto
    s.clear()
    print(s)


# Métodos Matemáticos de Conjuntos
    - Imagine que temos dois conjuntos: Um contendo estudantes do curso de Python e um
    contendo estudantes do curso de Java.

    estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
    estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

    - Veja que alguns alunos que estudam Python também já estudaram Java.

    # Precisamos gerar um conjunto com nomes de estudantes únicos
        # Forma 1 - Utilizando union
            unicos1 = estudantes_python.union(estudantes_java)
            print(unicos1)

        # Forma 2 - utilizando o caractere pipe |
            unicos2 = estudantes_python | estudantes_java
            print(unicos2)

    # Precisamos gerar um conjunto de estudantes que estão em ambos os cursos
        # Forma 1 - Utilizando intersection
            ambos1 = estudantes_python.intersection(estudantes_java)
            print(ambos1)

        # Forma 2 - Utilizando o &
            ambos2 = estudantes_python & estudantes_java
            print(ambos2)

    # Precisamos gerar um conjunto de estudantes que não estejam em ambos os cursos
        so_python = estudantes_python.difference(estudantes_java)
        print(so_python)

        so_java = estudantes_java.difference(estudantes_python)
        print(so_java)


# Soma*, Valo Máximo*, Valor Mínimo*, Tamanho
    * Se os valores forem todos inteiros ou reais
    s = {1, 2, 3, 4, 5, 6}
    print(sum(s))
    print(max(s))
    print(min(s))
    print(len(s))

"""





