"""
8) Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. A fórmula de conversão é: C = K - 273,15, sendo C a temperatura em Celsius e K a temperatura em Kelvin.
"""

kelvin = float(input('Digite a temperatura em graus Kelvin K: \n'))

print(f'A temperatura em graus Celsius de {kelvin}K é: {kelvin-273.15}ºC')