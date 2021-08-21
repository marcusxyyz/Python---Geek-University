"""
Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
A fórmula de conversão é: C = 5.0 * (F - 32.0) / 9.0, sendo F a Temperatura em Fahrenheit
e C a temperatura em Celsius.
"""

F = float(input('Digite os graus em Fahrenheit: '))
C = ((F - 32.0) * 5.0) / 9.0

print(f'A conversão para Celsius é de {C:.2f}')
