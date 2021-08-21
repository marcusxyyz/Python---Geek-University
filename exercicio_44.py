"""
Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar
subindo a escada. Calcule e mostre quantos degraus o usúario deverá subir para
atingir seu objetivo.
"""

degrau = float(input('Digite a altura do degrau: (max 0.18) '))
altura = float(input('Qual altura deseja alcançar? '))

degrais = altura / degrau

print(f'deverá subir {int(degrais)} degrais para alcançar a altura de {altura}')
