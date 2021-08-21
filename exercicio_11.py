"""
Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h
(quilômetros por hora). A fórmula de conversão é: K = M * 3.6, sendo K a velocidade em
Km/h e M em m/s.
"""

M = float(input('Digite a velocidade em m/s: '))
K = M * 3.6

print(f'A velocidade {M} m/s convertida para Km/h é de {K}')
