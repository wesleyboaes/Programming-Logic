'''
31) [DESAFIO] Crie um jogo de JoKenPo (Pedra-Papel-Tesoura)
'''
player_1 = False
player_2 = False

while player_1 == player_2:

    player_1 = input('Player 1 enter rock, paper or scissors: ')
    player_2 = input('Player 2 enter rock, paper or scissors: ')

    if player_1 == 'rock':
        if player_2 == 'rock':
            print('Draw!')
        elif player_2 == 'paper':
            print('Player 2 won!')
        elif player_2 == 'scissors':
            print('Player 1 won!')
    elif player_1 == 'paper':
        if player_2 == 'rock':
            print('Player 1 won!')
        elif player_2 == 'paper':
            print('Draw!')
        elif player_2 == 'scissor':
            print('Player 2 won!')
    elif player_1 == 'scissors':
        if player_2 == 'rock':
            print('Player 2 won!')
        elif player_2 == 'paper':
            print('Player 1 won!')
        elif player_2 == 'scissors':
            print('Draw!')