'''
33) Escreva um programa para aprovar ou não o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
'''
house_value = float(input('Enter the house price: '))
salary = float(input('Enter your salary: '))
years = int(input('In how many years you will pay? '))

month_value = house_value / (years * 12)
can_pay = salary * 0.3

if month_value <= can_pay:
    print('Approved!')
else:
    print('Reproved!')