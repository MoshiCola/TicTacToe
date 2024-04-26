def scalingboard(board_size):
    fullboard = [i for i in range(0, board_size ** 2)]
    return fullboard

def print_scalingboard(fullboard, board_size):
    for row in range(0, board_size):
        print(row)


scalingboard(3)
print_scalingboard(9, 3)