'''
22) Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua situação em relação ao alistamento militar.
- Se estiver antes dos 18 anos, mostre em quantos anos faltam para o alistamento.
- Se já tiver depois dos 18 anos, mostre quantos anos já se passaram do alistamento.
'''
from datetime import datetime

birth_year = int(input('ENter your birth year: '))
year = datetime.now().year
age = year - birth_year
for_enlistment = 18 - age
after_enlistment = age - 18

if age < 18:
    print(f'You need to wait {for_enlistment} years')
elif age > 18:
    print(f'You have enlisted for {after_enlistment} years')
else:
    print('You must go to enlistment')