"""
06) Leia uma temperatura em gruas Celsius e apresente-a convertida em graus Fahrenheit. A fórmula de conversão é: F = C*(9.0/5.0)+32,sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
"""

celsius = float(input('Digite a temperatura em graus Celsius °C: \n'))

print(f'A temperatura em graus Fahrenheit de {celsius}ºC é : {celsius * (9.0 / 5.0) + 32}F')

