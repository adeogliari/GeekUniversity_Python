"""
Funções com Parâmetro (de entrada)

#Funções que recebem dados para serem processados dentro da mesma;
    Se a gente pensar em um programa qualquer, geralmente temos:
        entrada -> processamento -> saída

    Se pensarmos em uma função, já sabemos que temos funções que:
        - Não possuem entrada;
        - Não possuem saída;
        - Possuem entrada mas não possuem saída;
        - Não possuem entrada mas possuem saída;
        - Possuem entrada e saída;


# Refatorando uma função
    def quadrado(numero):
        return numero ** 2

    print(quadrado(7))


# Funções podem ter n parâmetros de entrada. Ou seja, podemos receber como entrada em uma função
quantos parâmetros forem necessários. Eles são separados por vírgula.
    def multiplica(num1, num2):
        return num1 * num2


    def outra (num1, b, msg):
        return (num1 + b) * msg


    print(multiplica(10, 20))
    print(outra(7, 10, 'geek '))

    - OBS: Se informarmos um número errado de parâmetros ou argumentos, teremos TypeError


# Nomeado parâmetros
    def nome_completo(nome, sobrenome):
        return f'Seu nome completo é {nome} {sobrenome}'

    # A diferença entre parâmetros e Argumentos
     - Parâmetros são variáveis declaradas na definição de uma função;
     - Argumentos são dados passados durante a execução de uma função;


    # A ordem dos parâmetros importa!
        nome = 'Ademir'
        sobrenome = 'Ogliari'
        print(nome_completo(sobrenome, nome)

    # Argumentos nomeados (Keyword Arguments)
        - Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos
        utilizar qualquer ordem.

        print(nome_completo(nome='Ademir', sobrenome='Ogliari'))
        print(nome_completo(sobrenome='Ogliari', nome='Ademir', ))

    # Erro comum na utilização do return
        def soma_impares(numeros):
            total = 0
            for num in numeros:
                if num % 2 != 0:
                    total = total + num
                return total # ----> Return encerra a função, deveria estar fora do for
"""