"""
Faça um programa que leia o valor de um produto e imprima o valor com Desconto, tendo
em vista que o desconto foi de 12%.
"""

valor = float(input('Digite o valor do produto: '))

desconto = valor - 0.12 * valor

print(f'O valor com o desconto será {desconto:.2f} R$')
