'''
34) O Índice de Massa Corpórea (IMC) é um valor calculado baseado na altura e no peso de uma pessoa. De acordo com o valor do IMC, podemos classificar o indivíduo dentro de certas faixas.
- abaixo de 18.5: Abaixo do peso
- entre 18.5 e 25: Peso ideal
- entre 25 e 30: Sobrepeso
- entre 30 e 40: Obesidade
- acima de 40: Obseidade mórbida
Obs: O IMC é calculado pela expressão peso/altura² (peso dividido pelo quadrado da altura)
'''
weight = float(input('Enter your weight: '))
height = float(input('Enter your height: '))

imc = weight / (height * height)

if imc < 18.5:
    print(f'IMC = {imc:.2f}! You are under weight!')
elif imc >= 18.5 and imc <= 25:
    print(f'IMC = {imc:.2f}! You are at the correct weight!')
elif imc > 25 and imc <= 30:
    print(f'IMC = {imc:.2f}! You are overweight!')
elif imc > 30 and imc <= 40:
    print(f'IMC = {imc:.2f}! You are obese!')
else:
    print(f'IMC = {imc:.2f}! You are morbidly obese!')