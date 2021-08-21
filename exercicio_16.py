"""
Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros.
A fórmula para conversão é: C = P * 2.54, sendo C o comprimento em centímetros e
P o comprimento em polegadas.
"""

P = float(input('Digite o valor do comprimento em polegadas: '))
C = P * 2.54

print(f'O valor convertido em cenímetros é {C:.2f}')
