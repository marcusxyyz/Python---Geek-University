"""
Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
A fórmula de conversão é: F = C * (9.0 / 5.0) + 32.0, sendo F a Temperatura em Fahrenheit
e C a temperatura em Celsius.
"""

C = float(input('Digite a temperatura em Celsius: '))
F = C * (9.0 / 5.0) + 32.0

print(f'A temperatura em Fahrenheit é de {F:.2f}')
