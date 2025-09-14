'''
26) Escreva um algoritmo que leia dois números inteiros e compare-os, mostrando na tela uma das mensagens abaixo:
- O primeiro valor é o maior
- O segundo valor é o maior
- Não existe valor maior, os dois são iguais
'''
num_1 = int(input('Type the first number: '))
num_2 = int(input('Type the second number: '))

if num_1 > num_2:
    print(f'{num_1} is greater than {num_2}')
elif num_2 > num_1:
    print(f'{num_2} is greater than {num_1}')
else:
    print(f'{num_1} is equal to {num_2}')