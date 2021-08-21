"""
Leia uma velocidade em Km/h (Quilômetros por hora) e apresente-a convertida em m/s
(metros por segundo). A fórmula de conversão é: M = K / 3.6. sendo K a velocidade em
Km/h e M em m/s.
"""

K = float(input('Digite a velocidade em Km/h: '))
M = K / 3.6

print(f'A velocidade {K} em m/s é de {M:.2f}')
