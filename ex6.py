'''
6) Faça um programa que leia um número inteiro e mostre o seu antecessor e seu
sucessor.
Ex:
Digite um número: 9
O antecessor de 9 é 8
O sucessor de 9 é 10
'''
number = int(input('Type a number: '))
predecessor = number - 1
successor = number + 1
print(f'The predecessor of {number} is {predecessor}')
print(f'The successor of {number} is {successor}')