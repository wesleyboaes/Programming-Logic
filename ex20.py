'''
20) Desenvolva um programa que leia um número inteiro e mostre se ele é PAR ou ÍMPAR.
'''
number = int(input('Type a number: '))

if number % 2 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')