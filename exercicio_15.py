"""
Leia um ângulo em radianos e apresente-o convertido em graus. A fórmula de conversão
é: G = R * 180 / pi, sendo G o ângulo em graus e R em radianos e pi = 3.14.
"""

pi = 3.14

R = float(input('Digite o ângulo em radianos: '))
G = R * 180 / pi

print(f'O valor convertido em graus é {G:.2f}')
