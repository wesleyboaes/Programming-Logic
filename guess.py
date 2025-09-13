'''
Escreva um programa que, ao iniciar gera um valor aleatório de 1 a 10 e
permite que o usuário chute um número até que o valor aleatório gerado no
início do programa seja chutado corretamente.

O programa deve informar se o chute foi acima, abaixo ou igual ao valor
aleatório gerado no início do programa.

# Método 5Q's para montar um algorítimo:

Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais
informações/investigue mais até você compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
- Valor aleatório de 1 a 10

2. O que devo fazer com estes dados?
- Verificar se o chute dado foi maior, menor ou igual o valor aleatório

3. Quais são as restrições deste problema?
- Valor entre 1 e 10

4. Qual é o resultado esperado?
- Chute igual o valor

5. Qual é sequência de passos a ser feitas para chegar ao resultado esperado?
valor aleatório
input chute
if chute maior valor
    print Maior
if chute menor valor
    print Menor
if chute igual valor
    print acertou
'''
import random

valor = random.randint(1, 10)
chute = 0
while chute != valor:
    chute = int(input('Digite um valor: '))
    if chute > valor:
        print('Você escolheu um número maior')
    elif chute < valor:
        print('Você escolheu um número menor')
    else:
        print('Parabéns, você acertou')