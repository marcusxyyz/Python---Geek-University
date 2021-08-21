"""
Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-se
que esse funcionário tem uma gratificação de 5% sobre o salário-base. Além disso, ele
paga 7% de imposto sobre o salário-base.
"""

salarioBase = float(input('Informe o salário-base: '))

gratificacao = salarioBase * 0.05 + salarioBase

salarioImposto = 1000 * 0.07 + 1000

salarioTotal = salarioImposto - gratificacao + salarioBase

print(f'Salario recebido = {salarioTotal:.2f} R$')
