'''
30) [DESAFIO] Refaça o algoritmo 25, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais
- ESCALENO: todos os lados diferentes
'''
side_a = int(input('Enter side A: '))
side_b = int(input('Enter side B: '))
side_c = int(input('Enter side C: '))

if side_a > side_b + side_c:
    print('Can not be a triangle')
elif side_b > side_a + side_c:
    print('Can not be a triangle')
elif side_c > side_a + side_b:
    print('Can not be a triangle')
else:
    print('Can be a triangle')

if side_a == side_b and side_a == side_c:
    print('This is an equilateral triangle!')
elif side_a != side_b and side_a != side_c and side_b != side_c:
    print('This is a scalene triangle!')
else:
    print('This is an isosceles triangle!')