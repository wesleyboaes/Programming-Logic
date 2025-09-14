'''
32) [DESAFIO] Crie um jogo onde o computador vai sortear um número entre 1 e 5 o jogador vai tentar descobrir qual foi o valor sorteado.
'''
import random

number = random.randint(1, 5)
guess = 0

while guess != number:
    guess = int(input('Enter a number between 1 and 5: '))

    if guess > number:
        print('Choose a smaller number!')
    elif guess < number:
        print('Choose a greater number!')
    else:
        print('Congrats! You got it right!')