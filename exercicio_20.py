"""
Leia um valor da massa em quilogramas e apresente-o convertido em libras. A fórmula
de conversão é : L = k / 0.45, sendo K a massa em quilogramas e L a massaem libras.
"""

K = float(input('Digite o valor da massa em quilogramas: '))
L = K / 0.45

print(f'O valor da massa em libras é de {L:.2f}')
