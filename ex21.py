'''
21) Faça um algoritmo que leia um determinado ano e mostre se ele é ou não BISSEXTO.
'''
year = int(input('Type an year: '))

if year % 100 == 0:
    if year % 400 == 0:
        print('Is a leap year')
    else:
        print('Is not a leap year')
elif year % 4 == 0:
    print('Is a leap year')
else:
    print('Is not a leap year')