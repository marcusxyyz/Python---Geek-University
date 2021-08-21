"""
Leia um valor de comprimento em metros e apresente-o convertido em jardas. A
Fórmula de conversão é:J = M / 0.91 o comprimento em jardas é M o comprimento
em metros.
"""

M = float(input('Digite o valor do comprimento em metros: '))
J = M / 0.91

print(f'O valor do comprimento em jardas é {J:.2f}')
