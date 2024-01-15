# grid for the tic tac toe game
game_grid = [['   ', ' A ', ' | ', ' B ', ' | ', ' C '],
             [' 1 ', '   ', ' | ', '   ', ' | ', '   '],
             ['   ', '---', '-|-', '---', '-|-', '---'],
             [' 2 ', '   ', ' | ', '   ', ' | ', '   '],
             ['   ', '---', '-|-', '---', '-|-', '---'],
             [' 3 ', '   ', ' | ', '   ', ' | ', '   '], ]

magic_square = [[0, 0, 0, 0, 0, 0],
                [0, 8, 0, 1, 0, 6],
                [0, 0, 0, 0, 0, 0],
                [0, 3, 0, 5, 0, 7],
                [0, 0, 0, 0, 0, 0],
                [0, 4, 0, 9, 0, 2]]


# print the grid in the console
def print_grid():
    for row in range(6):
        temp = ''
        for col in range(6):
            temp += game_grid[row][col]
        print(temp)


def put_mark_on_grid(row, col, player):
    if player == 1:
        mark = ' X '
    else:
        mark = ' O '
    game_grid[row][col] = mark

def check_cell_empty(row, col):
    return game_grid[row][col] == '   '

def check_winner(row, col, player):
    if player == 1:
        mark = ' X '
    else:
        mark = ' O '

    #check the row
    if (game_grid[row][1] == mark) and (game_grid[row][3] == mark) and (game_grid[row][5] == mark):
        print("Winning row")
        return True

    #check the column
    if (game_grid[1][col] == mark) and (game_grid[3][col] == mark) and (game_grid[5][col] == mark):
        print("Winning column")
        return True

    #check the diagonal
    if (game_grid[1][1] == mark) and (game_grid[3][3] == mark) and (game_grid[5][5] == mark):
        print("Winning diagonal")
        return True

    # check the diagonal
    if (game_grid[5][1] == mark) and (game_grid[3][3] == mark) and (game_grid[1][5] == mark):
        print("Winning diagonal")
        return True

    return False

def check_full_board():
    #counts the number of empty cells
    count = 0
    for row in range(1, 6, 2):
        for col in range(1, 6 ,2):
            if game_grid[row][col] == '   ':
                count+=1
    return count==0

player = 1
game_is_on = True

while game_is_on:
    print_grid()
    move = input(f'Player {player}, where do you want to put your mark (column letter - row number? ').lower()
    if move[0] in ('a', 'b', 'c') and move[1] in ('1', '2', '3'):
        row = 2 * int(move[1]) - 1
        col = 2 * (ord(move[0]) - 96) - 1
        if check_cell_empty(row, col):
            put_mark_on_grid(row, col, player)
            if check_winner(row, col, player):
                game_is_on = False
                print(f"Congratulations to player {player}, you won!")
            else:
                if player == 1:
                    player = 2
                else:
                    player = 1
        else:
            print("Cell is already marked, please try another one")
    else:
        print("Invalid move, please try again (or type 'end' to forfeit).")

    if check_full_board():
        game_is_on = False
        print("It is a draw.")

    if move == 'end':
        game_is_on = False
        if player == 1:
            player = 2
        else:
            player = 1
        print(f"Congratulations to player {player}, you won!")

print_grid()

