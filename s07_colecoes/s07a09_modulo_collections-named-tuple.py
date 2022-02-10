"""
Módulo Collections - Named Tuple

Named Tuple -> São tuplas, diferenciadas, onde especificamos um nome para a mesma e também
parâmetros.
"""

# Importando

from collections import namedtuple

# Precisamos definir o nome e parâmetros.

# Forma 1 - Declaração Named Tuple
cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaração Named Tuple
cachorro = namedtuple('cachorro', 'idade,  raca, nome')

# Forma 3 - Declaração Named Tuple
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando a Named Tuple
ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')

# Acessando dados
# Forma 1
print(ray[0])

# Forma 2
print(ray.nome)