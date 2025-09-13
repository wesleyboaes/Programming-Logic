'''
17) Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse 80Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida.
'''
spd = float(input('Enter the speed: '))
fine = (spd - 80) * 5

if spd > 80:
    print(f'Your speed is above the allowed, you must pay {fine:.2f}')
else:
    print('Have a good travel!')