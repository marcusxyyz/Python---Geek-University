"""
Leia uma distância em quilômetros e apresente-a convertida em milhas. A fórmula de conversão é
M = K / 1.61, sendo K a distância em quilômetros e  M em milhas.
"""

K = float(input('Digite a distância em quilômetros: '))
M = K / 1.61

print(f'A distância em milhas é {M:.2f}')
