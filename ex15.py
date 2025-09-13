'''
15) Crie um programa que leia o número de dias trabalhados em um mês e mostre o salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$25 por hora trabalhada.
'''

days_worked = int(input('Enter the number of worked days: '))
salary = days_worked * 8 * 25

print(f'Your salary is {salary:.2f}')