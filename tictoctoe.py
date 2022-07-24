import random
from datetime import datetime
start_time = datetime.now()

print('welcome to the game, have fun')

print('choose the player type:')
player_type = int(input('1. player vs computer , 2. player vs player'))

def show_game_board():
    for i in range(3):     # in tedad satrha ast ( chand khat zir ham)
        for j in range(3): # in tedad sotonha ast
            print(game[i][j], end=' ')  # albate baray moshakhas kardan adad range , dar paeen khode game board moshakhas shode va aval ono bayad keshid.
        print()

def check():
    if game[0][0] == "x" and game[0][1] == 'x' and game[0][2] == 'x':
        print('player 1 wins')
        exit()

    if game[0][0] == "o" and game[0][1] == 'o' and game[0][2] == 'o':
        print('player 2 wins')
        exit()

    if game[0][0] == "O" and game[0][1] == 'O' and game[0][2] == 'O':
        print('computer wins')
        exit()    
#############################################################
    if game[1][0] == "x" and game[1][1] == 'x' and game[1][2] == 'x':
        print('player 1 wins')
        exit()

    if game[1][0] == "o" and game[1][1] == 'o' and game[1][2] == 'o':
        print('player 2 wins')
        exit()

    if game[1][0] == "O" and game[1][1] == 'O' and game[1][2] == 'O':
        print('computer wins')
        exit()
#############################################################
    if game[2][0] == "x" and game[2][1] == 'x' and game[2][2] == 'x':
        print('player 1 wins')
        exit()

    if game[2][0] == "o" and game[2][1] == 'o' and game[2][2] == 'o':
        print('player 2 wins')
        exit()

    if game[2][0] == "O" and game[2][1] == 'O' and game[2][2] == 'O':
        print('computer wins')
        exit()
#############################################################
#############################################################
    if game[0][0] == "x" and game[1][0] == 'x' and game[2][0] == 'x':
        print('player 1 wins')
        exit()

    if game[0][0] == "o" and game[1][0] == 'o' and game[2][0] == 'o':
        print('player 2 wins')
        exit()

    if game[0][0] == "O" and game[1][0] == 'O' and game[2][0] == 'O':
        print('computer wins')
        exit()    
#############################################################
    if game[0][1] == "x" and game[1][1] == 'x' and game[2][1] == 'x':
        print('player 1 wins')
        exit()

    if game[0][1] == "o" and game[1][1] == 'o' and game[2][1] == 'o':
        print('player 2 wins')
        exit()

    if game[0][1] == "O" and game[1][1] == 'O' and game[2][1] == 'O':
        print('computer wins')
        exit()
#############################################################
    if game[0][2] == "x" and game[1][2] == 'x' and game[2][2] == 'x':
        print('player 1 wins')
        exit()

    if game[0][2] == "o" and game[1][2] == 'o' and game[2][2] == 'o':
        print('player 2 wins')
        exit()

    if game[0][2] == "O" and game[1][2] == 'O' and game[2][2] == 'O':
        print('computer wins')
        exit()
#############################################################
#############################################################
    if game[0][0] == "x" and game[1][1] == 'x' and game[2][2] == 'x':
        print('player 1 wins')
        exit()

    if game[0][0] == "o" and game[1][1] == 'o' and game[2][2] == 'o':
        print('player 2 wins')
        exit()

    if game[0][0] == "O" and game[1][1] == 'O' and game[2][2] == 'O':
        print('computer wins')
        exit()    
#############################################################
    if game[0][2] == "x" and game[1][1] == 'x' and game[2][0] == 'x':
        print('player 1 wins')
        exit()

    if game[0][2] == "o" and game[1][1] == 'o' and game[2][0] == 'o':
        print('player 2 wins')
        exit()

    if game[0][2] == "O" and game[1][1] == 'O' and game[2][0] == 'O':
        print('computer wins')
        exit()
    
    else:
        print('draw')


game = [['_','_','_'],
        ['_','_','_'],
        ['_','_','_']]

show_game_board()

if player_type == 1 :
    while True:
        print('player 1')
        while True:
            row = int(input('satr ra vared konid: '))
            col = int(input('sotoon ra vared konid: '))
            if 0 <= row <= 2 and 0 <= col <= 2 :
                if game[row][col] == '_':
                    game[row][col] = 'x'
                    break
                else:
                    print('cell is not empty! ')

            else:
                print('index out of range, try again! ')


        show_game_board()
        check()

        print('computer')

        while True:
            row = random.randint(0,2)
            col = random.randint(0,2)
            if 0 <= row <= 2 and 0 <= col <= 2 :
                if game[row][col] == '_':
                    game[row][col] = 'O'
                    break
                else:
                    print('cell is not empty! ')

            else:
                print('index out of range, try again! ')


        show_game_board()
        check()
        end_time = datetime.now()
        print('zaman separi shode: {}'.format(end_time - start_time))


elif player_type == 2 :
    while True:
        print('player 1')
        while True:
            row = int(input('satr ra vared konid: '))
            col = int(input('sotoon ra vared konid: '))
            if 0 <= row <= 2 and 0 <= col <= 2 :
                if game[row][col] == '_':
                    game[row][col] = 'x'
                    break
                else:
                    print('cell is not empty! ')

            else:
                print('index out of range, try again! ')


        show_game_board()
        check()

        print('player 2')

        while True:
            row = int(input('satr ra vared konid: '))
            col = int(input('sotoon ra vared konid: '))
            if 0 <= row <= 2 and 0 <= col <= 2 :
                if game[row][col] == '_':
                    game[row][col] = 'o'
                    break
                else:
                    print('cell is not empty! ')

            else:
                print('index out of range, try again! ')


        show_game_board()
        check()
        end_time = datetime.now()
        print('zaman separi shode: {}'.format(end_time - start_time))
