""""
Loop for

Loop -> Estrutura de repetição
For -> Uma dessas estruturas


#C ou Java
for(int i = 0; i < limitador; i++ {
    //execução do loop
}


#Python
for item in interavel:
    //execução do loop


Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
- String
    nome = 'Geek University'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range (1, 10)


# Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra)

Enumerate:

nome = 'Geek University'
for indice, letra in enumerate(nome):
    print(nome[indice], end='')
Geek University

OBS= Por default o final do print possui o parâmetro \n, o end='' altera esse parâmetro

for valor in enumerate(nome):
    print(valor)
(0, 'G')
(1, 'e')
(2, 'e')
(3, 'k')
(4, ' ')
(5, 'U')
(6, 'n')
(7, 'i')
(8, 'v')
(9, 'e')
(10, 'r')
(11, 's')
(12, 'i')
(13, 't')
(14, 'y')

for indice, _ in enumerate(nome):
    print(indice)
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
OBS: Quando não precisamos de um valor, podemos descartá-lo utilizando um underline (_)


# Exemplo de for 2 (iterando sobre uma lista)
for numero in lista:
    print(numero)

lista = [1, 3, 5, 7, 9]


# Exemplo de for 3 (Iterando sobre um range)
range(valor_inicial, valor_final)

range = 10
for numero in range(1, range):
    print(numero)
1
2
3
4
5
6
7
8
9
10 -> Não
OBS: O valor final não é inclusive.


qtd = int(input('Quantas vezes esse loop deve rodar? \n'))
soma = 0

for n in range(1, qtd+1):
    num = float(input(f'Informe o valor {n} de {qtd}: \n'))
    soma = soma + num
print(f'A soma é {soma}')


emoji = '\U0001F60D'

for num in range(1, 11):
    print(f'{emoji * num}')
"""