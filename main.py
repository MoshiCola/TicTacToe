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
    

def whos_turn_is_it_anyway(current_player):
    if current_player == 'X':
        return 'O'
    else:
        return 'X'  

def moves(player, current_board):
    player_input = input(f'What spot chuwant {player}?:   ')
    spot = int(player_input)
    while current_board[spot] == spot:
            current_board[spot] = player
            print(current_board)
    game_over = win_cases(current_board)
    return current_board, game_over


gameboard = [0, 1, 2, 3, 4, 5, 6, 7, 8]
player = 'X'
game_over = False

while game_over == False:
    gameboard, game_over = moves(player, gameboard)
    player = whos_turn_is_it_anyway(player)