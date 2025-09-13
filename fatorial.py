'''
Crie um programa que recebe um número e imprime o seu fatorial.

# Método 5Q's para montar um algorítimo:

Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais
informações/investigue mais até você compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
numero

2. O que devo fazer com estes dados?
eu devo calcular o fatorial do número que for passado para o meu programa e o exibir na tela.

3. Quais são as restrições deste problema?
- O número deve ser um valor positivo
- O número deve ser um valor inteiro

4. Qual é o resultado esperado?
- O resultado esperado neste caso é que o fatorial do número informado seja exibido.

5. Qual é sequência de passos a ser feitas para chegar ao resultado esperado?
input numero
if numero > 0
if numero = inteiro
fatorial = 1
loop de 1 a numero
    fatorial = fatorial * numero
    numero = numero - 1
print fatorial
'''

numero = int(input('Digite um numero: '))
fatorial = 1

if numero < 0:
    print('O número digitado precisa ser positivo!')
else:
    for item in range(1, numero + 1):
        fatorial = fatorial * item
    print(f'O fatorial de {numero} é: {fatorial}')