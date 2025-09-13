'''
25) [DESAFIO] Crie um programa que leia o tamanho de três segmentos de reta. Analise seus comprimentos e diga se é possível formar um triângulo com essas retas. Matematicamente, para três segmentos formarem um triângulo, o comprimento de cada lado deve ser menor que a soma dos outros dois.
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