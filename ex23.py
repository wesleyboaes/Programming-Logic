'''
23) Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos para todos, mas especialmente para mulheres. Faça um programa que leia nome, sexo e o valor das compras do cliente e calcule o preço com desconto. Sabendo que:
- Homens ganham 5% de desconto
- Mulheres ganham 13% de desconto
'''
name = input('Enter your name: ')
sex = input('Enter your sex, male or female: ')
value = float(input('Enter the value of your purchases: '))
male_discount = value * 0.95
female_discount = value * 0.87

if sex == 'male':
    print(f'{name} your discounted purchases cost {male_discount:.2f}')
elif sex == 'female':
    print(f'{name} your discounted purchases cost {female_discount:.2f}')
else:
    print('You did not typed a correct value.')