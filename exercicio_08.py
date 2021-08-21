"""
Leia uma temperatura em graus Kelvin e apresente-a convertida em Graus Celsius. A
Fórmula de conversão é: C = K - 273.15, Sendo C a temperatura em Celsius e K a
temperatura em Kelvin.
"""

K = float(input('Digite a temperatura em graus Kelvin: '))
C = K - 273.15

print(f'A temperatura convertida em graus Celsius é {C:.2f}')
