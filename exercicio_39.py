"""
A importância de R$ 780_000_000 será dividida entre três ganhadores de um concurso.
Sendo que da quantia total:
    .O primeiro ganhador receberá 46%;
    .O segundo ganhador receberá 32%;
    .O terceiro o restante;
Calcule e imprima a quantia ganha por cada um dos ganhadores.
"""

premio = 780000000

primeiro = float(input('Qual a porcentagem que o primeiro ganhador receberá? '))
segundo = float(input('Qual a porcentagem que o segundo ganhador receberá? '))
terceiro = float(input('Qual a porcentagem que o terceiro ganhador receberá? '))

premio1 = primeiro / 100 * premio
premio2 = segundo / 100 * premio
premio3 = terceiro / 100 * premio

premioT = premio1 + premio2 + premio3

print(f'O primeiro ganhador recebeu {premio1:.2f} R$')
print(f'O segundo ganhador recebeu {premio2:.2f} R$')
print(f'e o terceiro ganhador recebeu {premio3:.2f} R$')
print(f'O total era {premioT}')


