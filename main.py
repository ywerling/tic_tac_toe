# grid for the tic tac toe game
game_grid = [['   ', ' A ', ' | ', ' B ', ' | ', ' C '],
             [' 1 ', '   ', ' | ', '   ', ' | ', '   '],
             ['   ', '---', '-|-', '---', '-|-', '---'],
             [' 2 ', '   ', ' | ', '   ', ' | ', '   '],
             ['   ', '---', '-|-', '---', '-|-', '---'],
             [' 3 ', '   ', ' | ', '   ', ' | ', '   '], ]


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


player = 2
game_is_on = True

while game_is_on:
    if player == 1:
        player = 2
    else:
        player = 1

    print_grid()
    move = input(f'Player {player}, where do you want to put your mark (column letter - row number? ').lower()
    if move[0] in ('a', 'b', 'c') and move[1] in ('1', '2', '3'):
        row = 2 * int(move[1]) - 1
        col = 2 * (ord(move[0]) - 96) - 1
        put_mark_on_grid(row, col, player)

    if move == 'end':
        game_is_on = False
