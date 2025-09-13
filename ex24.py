'''
24) Faça um algoritmo que pergunte a distância que um passageiro deseja percorrer em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para viagens até 200Km e R$0.45 para viagens mais ongas.
'''
distance = int(input('Enter the distance in kilometers: '))
short = distance * 0.5
long = distance * 0.45

if distance <= 200:
    print(f'The price is {short:.2f}')
else:
    print(f'The price is {long:.2f}')