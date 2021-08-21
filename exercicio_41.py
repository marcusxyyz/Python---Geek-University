"""
Faça um programa que leia o valor da hora de trabalho ( em reais) e número de horas
trabalhados no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre o valor calculado.
"""

valor = float(input('Qual o valor por hora trabalhada? '))
hora = int(input('Número de horas trabalhadas: '))

pagamento = valor * hora * 1.1

print(f'O pagamento recebido será {pagamento:.2f} R$')
