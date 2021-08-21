"""
Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão
é: R = G * pi / 180, sendo G o ângulo em graus e R em radianos e pi = 3.14.
"""

pi = 3.14

G = float(input('Digite o valor do ângulo em graus: '))
R = G * pi / 180

print(f'O valor em radianos é {R}')
