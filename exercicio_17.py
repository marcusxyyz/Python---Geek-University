"""
Leia um valor de comprimento em centímetros e apresente-o convertido em polegadas.
A fórmula para conversão é: P = C / 2.54, sendo C o comprimento em centímetros e
P o comprimento em polegadas.
"""

C = float(input('Digite o valor do comprimento em centímetros: '))
P = C / 2.54

print(f'O valor convertido em polegadas é de {P:.2f}')

