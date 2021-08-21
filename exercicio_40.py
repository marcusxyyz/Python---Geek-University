"""
Uma empresa contrata um encanador por R$ 30.00 o dia. Faça um programa
que solicite o número de dias trabalhados pelo encanador e imprima a quantia
líquida que deverá ser paga, sabendo-se que são descontados 8% para imposto de renda.
"""

dia = 30.00

diaria = int(input('Quantos dias trabalhados? '))

pagamento = diaria * dia
salario = pagamento + pagamento * 8 / 100

print(f'O salário recebido será = {salario:.2f}')
