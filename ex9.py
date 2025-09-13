'''
9) Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$) e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$5,35.
'''
real = float(input('How much reais do you have? '))
dollar = real * 5.35

print(f'Your R$ {real:.2f} reais is equal to $ {dollar:.2f} dollars.')