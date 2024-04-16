import random
from sys import exit
def win_cases(player, board):
    win_shiii = [[0, 1, 2],[3, 4, 5],[6, 7, 8],[0, 3, 6],[1, 4, 7],[2, 5, 8],[0, 4, 8],[2, 4, 6]]
    for combo in win_shiii:
        if board[combo[0]] == board[combo[1]] == board[combo[2]]:
            cool_board(board)
            print(f"{player} you've won!")
            run()
            return True
    return False


def saver(player, board, game_choice, letter_choice):
    new_board = [str(i) for i in board]
    with open('saved_game.txt', 'w') as save:
        save.write("".join(new_board) + '\n' + player + '\n' + game_choice + '\n' + letter_choice)


def loader(): 
    with open('saved_game.txt', 'r') as save:
        data = save.read().split('\n')
        board = data[0]
        player = data[1]
        game_choice = data[2]
        letter_choice = data[3]
        if game_choice.upper == 'COM':
            computer(player, board, game_choice, letter_choice)
        else:
            PVP(player, board, game_choice, letter_choice)
        
def issa_tie(board):
    for int in board:
        string = str(int)
        if string.isdigit():
            return False
    print('Issa tie. Double L')
    return True
        

def cool_board(current_board):
    print(f"┌───┬───┬───┐")
    print(f"│ {current_board[0]} │ {current_board[1]} │ {current_board[2]} │")
    print(f"│ {current_board[3]} │ {current_board[4]} │ {current_board[5]} │")
    print(f"│ {current_board[6]} │ {current_board[7]} │ {current_board[8]} │")
    print(f"└───┴───┴───┘")
    

def whos_turn_is_it_anyway(current_player):
    if current_player == 'X':
        return 'O'
    
    return 'X'

def computer_move(player, board):
    while True:
        try: 
            random_spot = random.randint(0, 8)
            if board[random_spot] != 'X' and board[random_spot] != 'O':
                board[random_spot] = player
                cool_board(board)
                game_over = win_cases(player, board)
                return board, game_over
        except IndexError:
            continue


def player_moves(player, current_board, game_choice, letter_choice):
    cool_board(current_board)
    player_input = input(f'What spot chuwant {player}?:   ')
    if player_input.upper() == 'SAVE':
        print('saved! noice!')
        saver(player, current_board, game_choice, letter_choice)
        run()
    if player_input.upper() == 'EXIT':
        exit()
    try:
        if current_board[int(player_input)] == int(player_input):
                current_board[int(player_input)] = player
    except: IndexError
    else:
        print('Pick a valid spot.')
    
    game_over = win_cases(player, current_board)
    return current_board, game_over

def PVP(player, gameboard, game_choice, letter_choice):
    game_over = False


    while True:

        try: 
            gameboard, game_over = player_moves(player, gameboard, game_choice, letter_choice)
            
            if game_over == False:
                game_over = issa_tie(gameboard)

            player = whos_turn_is_it_anyway(player)
        except IndexError:
            continue

def computer(player, gameboard, game_choice, letter_choice):
    game_over = False

    while game_over == False:
        while True:

            if letter_choice.upper() == "X":

                try:
                    gameboard, game_over = player_moves(player, gameboard, game_choice, letter_choice)
                    if game_over == False:
                        game_over = issa_tie(gameboard)
                    player = whos_turn_is_it_anyway(player)
                    gameboard, game_over = computer_move(player, gameboard)
                    if game_over == False:
                        game_over = issa_tie(gameboard)
                    player = whos_turn_is_it_anyway(player)
                    
                except IndexError:
                    continue
                    
            if letter_choice.upper() == 'O':
                try:
                    gameboard, game_over = computer_move(player, gameboard)
                    if game_over == False:
                        game_over = issa_tie(gameboard)
                    player = whos_turn_is_it_anyway(player)
                    gameboard, game_over = player_moves(player, gameboard, game_choice, letter_choice)
                    if game_over == False:
                        game_over = issa_tie(gameboard)
                    player = whos_turn_is_it_anyway(player)
                except IndexError:
                    continue



def run():
    gameboard = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    player = 'X'
    while True:
        game_choice = input(f'Type "load" to load a game. Type "PVP" for 2 players. Type "COM" for 1 player. Type "exit" to leave:  ')
        if game_choice.upper() == 'LOAD':
             print('Loading the game')
             loader()
             break
        if game_choice.upper() == 'EXIT':
            print('You Exit')
            exit()
        if game_choice.upper() == 'PVP':
            print('2 Player')
            letter_choice = 'X'
            PVP(player, gameboard, game_choice, letter_choice)
        elif game_choice.upper() == 'COM':
            print('Computer')
            letter_choice = input(f'You want X or O?:  ')
            computer(player, gameboard, game_choice, letter_choice)
        else:
            print('Dont be weird pick something...')

run()