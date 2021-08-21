"""
Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido pro -
porcionalmente ao valor que cada um deu para  a realização da aposta. Faça um programa que
leia quanto cada apostador investiu, o valor do prêmio, e imprima quando cada um ganha -
ria do prêmio com base no valor investido.
"""

premio = float(input('Qual o valor do prêmio? '))
primeiro = float(input('Quantos reais o primerio investiu? '))
segundo = float(input('Quantos reais o segundo investiu? '))
terceiro = float(input('Quantos reais o terceiro investiu? '))

investimento = primeiro + segundo + terceiro

porcentagem1 = primeiro * 100 / investimento * premio
porcentagem2 = segundo * 100 / investimento * premio
porcentagem3 = terceiro * 100 / investimento * premio

print(f'O primeiro receberá {porcentagem1:.2f} R$')
print(f'O segundo receberá {porcentagem2:.2f} R$')
print(f'O terceiro receberá {porcentagem3:.2f} R$')
print(f'do total de {porcentagem1 + porcentagem2 + porcentagem3}')
