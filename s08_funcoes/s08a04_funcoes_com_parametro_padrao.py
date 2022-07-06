"""
Funções com Parâmetro Padrão (Default Paramters)
    - Funções onde a passagem de parâmetro seja opcional;

# Exemplo de função onde a passagem de parâmetro seja opcional
    print('Geek University')

    Print()


# Exemplo de função onde a passagem de parâmetro seja obrigatória
    def quadrado(numero):
        return numero ** 2

    print(quadrado(3))


# Exemplo de função com parâmetro default
    def exponencial(numero, potencia=2):
        return numero ** potencia


    print(exponencial(2))  # Eleva o primeiro argumento à potência 2 (padrão)
    print(exponencial(2, 3))  # Eleva o primeiro argumento à potência do segundo

    OBS: Em funções python, os parâmetros com valores default (padrão) DEVEM sempre estar ao
    final da declaração

# Exemplo mais complexo
    def mostra_informacao(nome='Geek', instrutor=False):
        if nome == 'Geek' and instrutor:
            return 'Bem vindo instrutor Geek!'
        elif nome == 'Geek':
            return 'Eu pensei que você era o instrutor'
        return f'Olá {nome}'

    print(mostra_informacao())
    print(mostra_informacao(instrutor=True))
    print(mostra_informacao('Ozzy'))
    print(mostra_informacao(nome='Stephany'))


# Escopo - Evitar problemas e confusões
    # Variáveis Globais
        instrutor = 'Geek' # Variável Global

        def diz_oi():
            instrutor = 'python'
            return f'Oi {instrutor}'

        def diz_oi():
            prof = 'Geek' # Variável local
            return f'Oi {prof}'

        print(diz_oi())
        print(prof) # NameError

        #ATENÇÃO com variáveis globais (se puder evitar, evite!)

        total = 0

        def incrementa():
            global total # Avisando que queremos utilizar a variável global

            total = total + 1
            return total

        print(incrementa())



    # Variáveis locais

        def fora():
            contador = 0

            def dentro():
                nonlocal contador
                contador += 1
                return contador
            return dentro()

        OBS: Se tivermos uma variável local com o mesmo nome de uma variável global,
        a local terá preferência
"""

