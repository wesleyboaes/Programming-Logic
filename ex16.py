'''
16) [DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule quantos dias de vida um fumante perderá e exiba o total em dias.
'''

cigarettes = int(input('How many cigarettes have you smoked per day?'))
years = int(input('For how many years? '))
days = years * 365
total_cigarettes = cigarettes * days
life_lost_min = total_cigarettes * 10
life_lost_days = life_lost_min / 24

print(f'You lost {life_lost_days:.0f} days of your life')