"""
Módulo Collection - Counter (contador)

Collections -> É conhecido como High-Performance Container Datatypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collection
Counter que é parecido com um dicionário, contendo como chave o elemento da lista que
passamos como parâmetro e como valor a quantidade de ocorrências desse elemento.

# Utilizando o Counter

# Importando o Counter
    from collections import Counter

    # Exemplo 1
        # Podemos utilizar qualquer iterável, aqui usamos uma lista
        lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 43, 34]

        res = Counter(lista)
        print(type(res))
        print(res)

        RESULTADO: Counter({1: 5, 3: 5, 2: 4, 5: 4, 4: 3, 45: 2, 66: 1, 43: 1, 34: 1})
        # Veja que para cada elemento da lista, o counter criou uma chave e colocou como
        valor a quantidade de ocorrências.

    # Exemplo 2
        print(Counter('Geek University'))
        # Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1,
        'r': 1, 's': 1, 't': 1, 'y': 1})

    # Exemplo 3
        texto = '''Foca foi a primeira classe naval de submarinos operados pela Marinha do Brasil.
                   Era composta pelo F1, F3 e F5, submarinos projetados pelo engenheiro naval Cesare
                   Laurenti e construídos em La Spezia, Itália. A classe fazia parte do programa
                   naval da marinha de 1906 para aquisição de navios de guerra com o intuito de
                   modernizá-la. Os submarinos foram adquiridos para servirem como plataforma de
                   treinamento e manutenção para as tripulações, com poucas ações navais no
                   decorrer dos 19 anos em que estiveram ativos. A marinha incorporou a classe em
                   17 de julho de 1914 e, com isso, ampliou sua estrutura naval para abrigar essa
                   nova arma como, por exemplo, a criação da'''

        palavras = texto.split()
        # print(palavras)

        res = Counter(palavras)
        # print(res)

        # Encontrando as 5 palavras com mais ocorrências no texto
        print(res.most_common(5))
"""

