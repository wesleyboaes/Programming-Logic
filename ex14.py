'''
14) A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar, sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado.
'''

distance = float(input('Enter the kilometers: '))
days = int(input('Enter the days: '))

price_distance = distance * 0.2
price_days = days * 90

total = price_distance + price_days

print(f'You must pay {total:.2f}')