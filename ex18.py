'''
18) Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade dela e depois mostre se ela pode ou não votar.
'''
from datetime import datetime

birth_year = int(input('Enter your birth day: '))
year = datetime.now().year
age = year - birth_year

if age < 16:
    print(f'You can not vote, you just have {age} years old')
else:
    print(f'You can vote, you have {age} years old')