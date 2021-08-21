"""
Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo
que ele recebeu um aumento de 25%.
"""

salario = float(input('Digite o antigo salário do funcionário: '))

novoSalario = ((25 / 100 + 1) * salario)

print(f'O novo sálario do funcionário é {novoSalario:.2f} R$')
