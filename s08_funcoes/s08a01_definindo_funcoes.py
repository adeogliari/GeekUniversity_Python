"""
Definindo Funções
    - Funções são pequenas partes de código que realizam tarefas específicas;
    - Podem ou n"ao receber entradas de dados e retornar saídas de dados;
    - Muito úteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela, é bom fazer uma
verificação para que a função seja simplificada


Já utilizamos várias funções desde que iniciamos este curso:
    - print()
    - len()
    - max()
    - min()
    - count()
    - e muitas outras;


# Exemplo de utilização de funções:
    # cores = ['verde', 'amarelo', 'azul', 'branco']

    # Utilizando a função integrada (Built-in) do Python print()

    # print(cores)

    # curso = 'Programação em Python: Essencial'

    # print(curso)

    # cores.append('roxo')

    # print(cores)

    # curso.append('Mais dados...') # AtrributeError
    # print(curso)

    # cores.clear()
    # print(cores)

    # print(help(print))

    # DRY - Don´t Repeat Yourself - Não repita você mesmo / Não repita seu código

# Mas então, como definir funções?
    # Em Python, a forma geral de definir uma função é:

        def nome_da_função(parametros_de_entrada):
            bloco_da_funcao

    onde:
        nome_da_função -> SEMPRE, com letras minúsculas, e se for nome composto, separado por
        underline (Snake Case)

        parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula,
        podendo ser opcionais ou não;

        bloco_da_funcao -> Também chamado de corpo da função ou implementação, é onde o
        processamento da função acontece. Neste bloco, pode ter ou não retorno da função.

    OBS: Veja que apara definir uma função, utilizamos a palavra reservada 'def' informando ao
    Python que estamos definindo uma função. Também abrimos o bloco de código com o já
    conhecido dois pontos: que é utilizado em Python para definir blocos.
    """

# Definindo a primeira função


def diz_oi():
    print('oi!')

"""
OBS:
    1- Veja que dentro das nossas funções podemos utilizar outras funções:
    2- Veja que nossa função só executa 1 tarefa, ou seja, a única coisa que ela faz é dizer oi;
    3- Veja que esta função não recebe nenhum parâmetro de entrada;
    4- Veja que esta função nao retorna nada;


# Utilizando funções
    # Chamada de execução
    # diz_oi()

    ATENÇÃO: Nunca esqueça de utilizar o parênteses ao executar uma função.

Exemplo:
    # Errado!
    diz_oi
    
    # Certo!
    diz_oi()
    
    # Errado!
    diz_oi ()
"""

# Exemplo 2


def cantar_parabens():
    print('Parabéns para você')
    print('Nesta data Querida')
    print('Muitas Felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante!')


# for n in range(5):
    # cantar_parabens()

# Em Python, podemos inclusive criar variáveis do tipo de uma função e executar esta função
# através da variável


cantar = cantar_parabens

cantar()

