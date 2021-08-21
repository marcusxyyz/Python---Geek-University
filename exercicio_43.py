"""
Escreva  um programa de ajuda para vendedores. A partir de um valor total lido,mostre:
o total a pagar com desconto de 10%.
o valor de cada parcela, no parcelamento de 3x sem juros.
a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)
"""

produto = float(input('Qual o valor do produto? '))

desconto10 = produto - produto * 0.1
parcela = produto / 3
comissaoVista = desconto10 * 0.05
comissaoParcelado = produto * 0.05

print(f'O valor com desconto de 10% é {desconto10:.2f} R$')
print(f'Parcelado em 3x o valor de cada parcela é {parcela:.2f} R$')
print(f'A comissão recebida pelo vendedor no valor a vista é {comissaoVista:.2f} R$')
print(f'A comissã recebida pelo vendedor no valor parcelado é {comissaoParcelado} R$')
