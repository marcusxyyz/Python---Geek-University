"""
Leia uma temperatura em graus Celsius e apresente-a convertida em Graus Kelvin. A
Fórmula de conversão é: K = C + 273.15, Sendo C a temperatura em Celsius e K a
temperatura em Kelvin.
"""

C = float(input('Digite a temperatura em graus Celsius: '))
K = C + 273.15

print(f'A temperatura convertida em graus Kelvin é {K:.2f}')
