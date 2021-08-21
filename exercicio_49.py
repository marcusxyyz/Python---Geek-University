"""
Faça um programa que leia (hora,minutos e segundos) de inicio e a duração de uma experiência,
em segundos, de uma experiência biológica.O programa deve resultar com o novo horário
(hora minutose segundos) do termino da mesma.
"""

hora = int(input('Que horas iniciou a experiência'))
minutos = int(input('Minutos: '))
segundos = int(input('Segundos: '))

horaS = hora * 3600
minutosS = minutos * 60
Tempo = horaS + minutosS + segundos

duracao = int(input('Qual será a duração? '))

total = Tempo + duracao

novaHora = horaS / 3600
novominuto = minutosS / 60

print(f'novo horario {novaHora}:{novominuto}')
