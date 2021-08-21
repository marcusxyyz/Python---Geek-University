"""
Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor
de seu dobro.
"""

num = int(input('Digite um número inteiro: '))

soma = ((num + 1) * 3) + ((num - 1) * 2 )

print(f'Resultado = {soma}')
