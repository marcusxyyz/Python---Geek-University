"""
Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro. O volume
de um cilindro circular é calculado por meio da seguinte fórmula: V = pi * raio² * altura,
onde pi = 3.141592.
"""

pi = 3.141592

altura = float(input('Digite a altura do cilindro: '))
raio = float(input('Digite o raio do cilindro: '))

V = pi * raio ** 2 * altura

print(f'Volume = {V:.2f}')
