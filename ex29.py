'''
29) Desenvolva um programa que leia o nome de um funcionário, seu salário, quantos anos ele trabalha na empresa e mostre seu novo salário, reajustado de acordo com a tabela a seguir:
- Até 3 anos de empresa: aumento de 3%
- entre 3 e 10 anos: aumento de 12.5%
- 10 anos ou mais: aumento de 20%
'''
name = input('Enter the name: ')
salary = float(input('Enter the salary: '))
years_company = int(input('Enter how many years of company: '))

small = salary * 1.03
medium = salary * 1.125
big = salary * 1.2

if years_company <= 3:
    print(f'New salary: $ {small:.2f}')
elif years_company >= 10:
    print(f'New salary: $ {big:.2f}')
else:
    print(f'New salary: $ {medium:.2f}')