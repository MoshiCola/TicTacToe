gameboard = [0, 1, 2, 3, 4, 5, 6, 7, 8]
x_moves = 0
o_moves = 0

game_over = False

    

def win_cases(board):
    if board[0] == board[1] == board[2]:
        return True

    if board[3] == board[4] == board[5]:
        return True

    if board[6] == board[7] == board[8]:
        return True

    if board[0] == board[3] == board[6]:
        return True

    if board[1] == board[4] == board[7]:
        return True

    if board[2] == board[5] == board[8]:
        return True

    if board[0] == board[4] == board[8]:
        return True

    if board[2] == board[4] == board[6]:
        return True
    else:
        return False
    

def whos_turn_is_it_anyway(last_thing_added_to_board):
    



def moves(player, current_board):
    player_input = input(f'What spot chuwant {player}?:   ')
    spot = int(player_input)
    if current_board[spot] == spot:
        current_board[spot] = player
    print(current_board)
    return game_over == win_cases(current_board)



while game_over == False:



    x_moves = input(f'What spot chuwant X?:   ')
    x_spot = int(x_moves)
    if gameboard[x_spot] == x_spot:
        gameboard[x_spot] = 'X'
    print(gameboard)
    game_over = win_cases(gameboard)

    o_moves = input(f'What spot chuwant O?:   ')
    o_spot = int(o_moves)
    if gameboard[o_spot] == o_spot:
        gameboard[o_spot] = 'O'
    print(gameboard)
    game_over = win_cases(gameboard)

    


        


