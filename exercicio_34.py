"""
Leia um valor  do raio de um círculo e Calcule e imprima a área do círculo correspondente.
A área do círculo é pi * raio², considere pi = 3.141592.
"""

pi = 3.141592

r = float(input('Qual o raio do círculo: '))
A = pi * r ** 2

print(f'Área = {A}')
