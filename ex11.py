'''
11) Desenvolva uma lógica que leia os valores de A, B e C de uma equação do segundo grau e mostre o valor de Delta.
'''
A = int(input('Enter with value of A: '))
B = int(input('Enter with value of B: '))
C = int(input('Enter with value of C: '))
delta = (B ^ 2) - 4 * A * C

print(f'Delta is {delta}')