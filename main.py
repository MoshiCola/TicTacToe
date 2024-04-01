import random
from sys import exit
def win_cases(board, player):
    win_shiii = [[0, 1, 2],[3, 4, 5],[6, 7, 8],[0, 3, 6],[1, 4, 7],[2, 5, 8],[0, 4, 8],[2, 4, 6]]
    for combo in win_shiii:
        if board[combo[0]] == board[combo[1]] == board[combo[2]]:
            cool_board(board)
            print(f"{player} you've won!")
            run()
            return True
    return False

        
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
                game_over = win_cases(board, player)
                return board, game_over
        except IndexError:
            continue


def moves(player, current_board):
    cool_board(current_board)
    player_input = input(f'What spot chuwant {player}?:   ')
    spot = int(player_input)
    if player_input.upper() == 'EXIT':
        exit()
    if current_board[spot] == spot:
            current_board[spot] = player
    else:
        print('Pick a valid spot.')
    
    game_over = win_cases(current_board, player)
    return current_board, game_over

def PVP():
    gameboard = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    player = 'X'
    game_over = False


    while True:

        try: 
            gameboard, game_over = moves(player, gameboard)
            
            if game_over == False:
                game_over = issa_tie(gameboard)

            player = whos_turn_is_it_anyway(player)
        except IndexError:
            continue

def computer():
    choice = input(f'Pick "X" or "O":   ')
    gameboard = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    player = 'X'
    game_over = False

    while game_over == False:
        while True:

            if choice.upper() == "X":

                try:
                    gameboard, game_over = moves(player, gameboard)
                    if game_over == False:
                        game_over = issa_tie(gameboard)
                    player = whos_turn_is_it_anyway(player)
                    gameboard, game_over = computer_move(player, gameboard)
                    if game_over == False:
                        game_over = issa_tie(gameboard)
                    player = whos_turn_is_it_anyway(player)
                    
                except IndexError:
                    continue
                    
            if choice.upper() == 'O':
                try:
                    gameboard, game_over = computer_move(player, gameboard)
                    if game_over == False:
                        game_over = issa_tie(gameboard)
                    player = whos_turn_is_it_anyway(player)
                    gameboard, game_over = moves(player, gameboard)
                    if game_over == False:
                        game_over = issa_tie(gameboard)
                    player = whos_turn_is_it_anyway(player)
                except IndexError:
                    continue



def run():
    while True:
        choice = input(f'Type "PVP" for 2 players. Type "COM" for 1 player. Type "exit" to leave:  ')
        if choice.upper() == 'EXIT':
            print('You Exit')
            exit()
        if choice.upper() == 'PVP':
            print('Player')
            PVP()
        elif choice.upper() == 'COM':
            print('Computer')
            computer()
        else:
            print('Dont be weird pick something...')

run()