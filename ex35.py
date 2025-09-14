'''
35) Uma empresa de aluguel de carros precisa cobrar pelos seus serviços. O aluguel de um carro custa R$90 por dia para carro popular e R$150 por dia para carro de luxo. Além disso, o cliente paga por Km percorrido. Faça um programa que leia o tipo de carro alugado (popular ou luxo), quantos dias de aluguel e quantos Km foram percorridos. No final mostre o preço a ser pago de acordo com a tabela a seguir:
- Carros populares (aluguel de R$90 por dia)
- Até 100Km percorridos: R$0,20 por Km
- Acima de 100Km percorridos: R$0,10 por Km
- Carros de luxo (aluguel de R$150 por dia)
- Até 200Km percorridos: R$0,30 por Km
- Acima de 200Km percorridos: R$0,25 por Km
'''
car_type = input('Enter the type of car, popular or luxury: ')
day = int(input('Enter how many days you will rent: '))
distance = int(input('Enter how many Kilometers you will travel: '))

popular_car = day * 90
luxury_car = day * 150

if car_type == 'popular':
    if distance <= 100:
        price = popular_car + (distance * 0.2)
    else:
        price = popular_car + (distance * 0.1)

elif car_type == 'luxury':
    if distance <= 200:
        price = luxury_car + (distance * 0.3)
    else:
        price = luxury_car + (distance * 0.25)

print(f'You choose a {car_type} car and traveled {distance}Km, the rental price is $ {price:.2f}')