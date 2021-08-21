"""
Faça um programa para ler as dimensões de um terreno (comprimento c e largura l),
bem como o preço do metro da tela p . imprima o custo para cercar este mesmo terreno
"""

C = float(input('Digite o comprimento do terreno: '))
L = float(input('Digite a Largura do terreno: '))

A = C * L

p = float(input('Quanto custa o metro da tela? '))

total = A * p

print(f'Valor da tela {total:.2f}')
