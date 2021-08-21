import math
"""
Escreva um programa que leia as coordenadas x e y de pontos no R2 e calcule sua distância da origem (0; 0).
"""

x = float(input('Digite o valor de x: '))
y = float(input('Digite o valor de y: '))

dist = math.sqrt((x ** 2) + (y ** 2))

print(dist)
