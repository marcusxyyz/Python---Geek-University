"""
Leia um valor inteiro em segundos, e imprima-o em horas,minutos e segundos.
"""

num = int(input('Digite um valor em segundos: '))

hora = num * 3600
minu = num * 60
seg = num

print(f'Horas {hora / 3600:.0f}:{minu / 120:.1f}:{seg / 60:.1f}')
