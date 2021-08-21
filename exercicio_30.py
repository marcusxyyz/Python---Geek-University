"""
Leia um valor em real e a cotação do dolar. Em seguida , imprima o valor correspondete em dólares.
"""

real = float(input('Digite o valor do real: '))
cot = float(input('Qual valor do dólar? '))

dolar = real / cot

print(f'O valor em real convertido em dólar é {dolar:.2f} US')
