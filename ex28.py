'''
28) Faça um programa que leia a largura e o comprimento de um terreno
retangular, calculando e mostrando a sua área em m². O programa também
devemostrar a classificação desse terreno, de acordo com a lista abaixo:
- Abaixo de 100m² = TERRENO POPULAR
- Entre 100m² e 500m² = TERRENO MASTER
- Acima de 500m² = TERRENO VIP
'''
width = float(input('Enter the width: '))
length = float(input('Enter the length: '))
area = width * length

if area < 100:
    print('Popular land')
elif area > 500:
    print('VIP land')
else:
    print('Master land')