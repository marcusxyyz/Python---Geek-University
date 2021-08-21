import math

"""
Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação:
hipotenusa = raizQ a² + b². Faça um programa que receba os valores de a e b e calcule
o valor da hipotenusa através da equação. imprima o resultado desta operação.
"""

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))

hipotenusa = math.sqrt(a ** 2 + b ** 2)

print(f'A hipotenusa do triângulo é = {hipotenusa}')
