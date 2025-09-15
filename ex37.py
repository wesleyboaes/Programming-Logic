'''
37) Uma empresa precisa reajustar o salário dos seus funcionários, dando um
aumento de acordo com alguns fatores. Faça um programa que leia o salário atual, o gênero do funcionário e há quantos anos esse funcionário trabalha na empresa. No final, mostre o seu novo salário, baseado na tabela a seguir:

- Mulheres
- menos de 15 anos de empresa: +5%
- de 15 até 20 anos de empresa: +12%
- mais de 20 anos de empresa: +23%

- Homens
- menos de 20 anos de empresa: +3%
- de 20 até 30 anos de empresa: +13%
- mais de 30 anos de empresa: +25%
'''

current_salary = float(input('Enter with your current salary: '))
gender = input('Enter your gender, man or woman: ')
years_company = int(input('Enter how many years you are in the company: '))

if gender == 'woman':
    if years_company < 15:
        new_salary = current_salary * 1.05
    elif years_company > 20:
        new_salary = current_salary * 1.23
    else:
        new_salary = current_salary * 1.12
elif gender == 'man':
    if years_company < 20:
        new_salary = current_salary * 1.03
    elif years_company > 30:
        new_salary = current_salary * 1.25
    else:
        new_salary = current_salary * 1.13

print(f'Your new salary is {new_salary:.2f}')        