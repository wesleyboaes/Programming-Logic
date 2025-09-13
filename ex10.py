'''
10) Faça um algoritmo que leia a largura e altura de uma parede, calcule e
mostre a área a ser pintada e a quantidade de tinta necessária para o serviço,
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
'''
width = float(input('What is the width of the wall? '))
height = float(input('What is the height of the wall? '))
area = width * height
can_paint = area / 2

print(f'To paint {area}m of wall you will need {can_paint:.0f} paint cans')