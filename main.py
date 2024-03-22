import random
from sys import exit
def win_cases(board, player):
    win_shiii = [[0, 1, 2],[3, 4, 5],[6, 7, 8],[0, 3, 6],[1, 4, 7],[2, 5, 8],[0, 4, 8],[2, 4, 6]]
    for combo in win_shiii:
        if board[combo[0]] == board[combo[1]] == board[combo[2]]:
            print(f"{player} you've won!")
            return True

        
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

# def computer_move():
    






def moves(player, current_board):
    cool_board(current_board)
    player_input = input(f'What spot chuwant {player}?:   ')
    spot = int(player_input)
    if current_board[spot] == spot:
            current_board[spot] = player
            cool_board(current_board)

    else:
         raise AttributeError('Spot does not exist')
    game_over = win_cases(current_board, player)
    return current_board, game_over

def PVP():
    gameboard = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    player = 'X'
    game_over = False

    while not game_over:
        try: 
            gameboard, game_over = moves(player, gameboard)
            if game_over == False:
                game_over = issa_tie(gameboard)
        except:
             print("That's not a spot g")
             continue
        player = whos_turn_is_it_anyway(player)

def computer():
    gameboard = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    player = 'X'
    game_over = False

    while not game_over:
        try: 
            if player == 'X':
                gameboard, game_over = moves(player, gameboard)
                if game_over == False:
                    game_over = issa_tie(gameboard)
            else:
                gameboard = computer_move()
                game_over = win_cases(gameboard, player)
                if game_over == False:
                    game_over = issa_tie(gameboard)
        except:
             print("That's not a spot g")
             continue
        player = whos_turn_is_it_anyway(player)


def menu():
    while True:
        choice = input(f'Type "PVP" for 2 players. Type "COM" for 1 player. Type "exit" to leave.')
        if choice == 'exit':
            print('You Exit')
            exit()
        if choice == 'PVP':
            print('Player')
            PVP()
        elif choice == 'COM':
            print('Computer')
            Computer()
        else:
            print('Dont be weird pick something...')

menu()