'''
7) Crie um algoritmo que leia um número real e mostre na tela o seu dobro e a
sua terça parte.
Ex:
Digite um número: 3.5
O dobro de 3.5 é 7.0
A terça parte de 3.5 é 1.16666
'''
number = float(input('Type a number: '))
double = number * 2
one_third = number/3

print(f'The double of {number} is {double:.2f}')
print(f'One third of {number} is {one_third:.5f}')