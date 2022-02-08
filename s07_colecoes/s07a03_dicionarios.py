"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos por
mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}

print(type({}))

OBS: Sobre Dicionários
    - Chave e valor são separados por dois pontos 'chave:valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;


# Criação de dicionários
    # Forma 1 (Mais Comum)
        paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
        print(paises)
        print(type(paises))

    # Forma 2 (Menos Comum)
        paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
        print(paises)
        print(type(paises))


# Acessando elementos
    paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

    # Forma 1 - Acessando via chave, da mesma forma que lista/tupla (NÃO RECOMENDADO)
        print(paises['br'])
        print(paises['ru']) # Retorna erro

    # Forma 2 - Acessando via get (RECOMENDADO)
        Caso o get não encontre o objeto com a chave informada, será retornado
        o valor None.
        print(paises.get('br'))
        print(paises.get('ru')) # Não retorna erro e sim um valor do tipo None

        russia = paises.get('ru')
        if russia:
            print('Encontrei a Rússia')
        else:
            print('Não encontrei a Russia')

        # Podemos definir um valor padrão caso não encontremos o objeto com a chave
        informada
            pais = paises.get('ru', 'Não encontrado')
            print(f'Encontrei o país {pais}')


# Podemos verificar se determinada chave se encongtra em um dicionário
    print('br' in paises)
    print('ru' in paises)
    print('Estados Unidos' in paises)

    if 'ru' in paises:
        russia = paises['ru']


# Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive
lista, tupla e dicionário como chaves de dicionários
    - Tuplas são bastante interessantes de serem utilizadas como chave de dicionários,
    pois as messas são imutáveis

    localidades = {
        (35.6895, 39.6917): 'Escritório em Tókio',
        (40.7128, 74.0060): 'Escritório em Nova York',
        (37.7749, 122.4194): 'Escritório em São Paulo'
    }

    print(localidades)
    print(type(localidades))


# Adicionar elementos em um dicionário
    receita = {'jan': 100, 'fev': 120, 'mar': 300}

    # Forma 1 - Mais comum
        receita['abr'] = 350
        print(receita)

    #Forma 2
        novo_dado = {'mai': 500}
        receita.update(novo_dado)
        print(receita)

# Atualizando dados em um dicionário

    # Forma 1
        receita['mai'] = 550
        print(receita)

    # Forma 2
        receita.update({'mai': 600})
        print(receita)

    CONCLUSÃO 1: A forma de adicionar novos elementos ou atualizar dados em um
                 dicionário é a mesma
    CONCLUSÃO 2: Em dicionários, NÃO podemos ter chaves repetidas


# Remover dados de um dicionário
    receita = {'jan': 100, 'fev': 120, 'mar': 300}
    print(receita)

    # Forma 1 (mais comum)
        ret = receita.pop('mar')
        print(ret)
        print(receita)

    # OBS 1: Quando usando pop, precisamos SEMPRE informar a chave
    # OBS 2: Ao removermos um objeto, o valor deste objeto é sempre retornado

    # Forma 2:
        del receita['fev']
        print(receita)

    # OBS: Neste caso, o valor removido não é retornado.


# Métodos de dicionários
    d = dict(a=1, b=2, c=3)
    # Limpar o Dicionário
        d.clear()
        print(d)

    # Copiando um dicionário para outro
        # Forma 1 - Deep Copy
            novo = d.copy()
            print(novo)

            novo['d'] = 4

            print(d)
            print(novo)

        # Forma 2 - Shallow Copy
            novo = d

            print(novo)

            novo['d'] = 4

            print(d)
            print(novo)


# Forma não usual de criação de dicionários
    outro = {}.fromkeys('a', 'b')

    print(outro)
    print(type(outro))

    usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
    print(usuario)
    print(type(usuario))

    # O método fromkeys recebe dois parâmetros: um iterável e um valor.
    # Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o
    valor informado

    veja = {}.fromkeys('abcde', 'valor')
    print(veja)

    veja = {}.fromkeys(range(1, 11), 'novo')
    print(veja)
"""





