def check_impossible(a):
    if abs(a.count('X') - a.count('O')) > 1:
        return True
    if check_win("X") and check_win("O"):
        return True


def check_not_finished(a):
    if a.count('X') + a.count('O') < 9:
        return True
    else:
        return False


def check_win(player):
    global cells
    if cells[0] == cells[1] == cells[2] == player \
            or cells[3] == cells[4] == cells[5] == player \
            or cells[6] == cells[7] == cells[8] == player \
            or cells[0] == cells[3] == cells[6] == player \
            or cells[1] == cells[4] == cells[7] == player \
            or cells[2] == cells[5] == cells[8] == player \
            or cells[0] == cells[4] == cells[8] == player \
            or cells[2] == cells[4] == cells[6] == player:
        return True


def coords_failed(x, y, grid):
    valid = ('1', '2', '3')
    occupied = ('X', 'O')
    if not x.isnumeric() or not y.isnumeric():
        print('Enter numbers!')
        return True
    elif x not in valid or y not in valid:
        print("Coordinates should be 1 to 3!")
        return True
    index = (((int(x) - 1) * 3) + (int(y) + 2)) - 3
    if grid[index] in occupied:
        print("That cell is occupied! Choose another one!")
        return True
    return False


def make_move(x, y, grid, player):
    index = (((int(x) - 1) * 3) + (int(y) + 2)) - 3
    if index == 0:
        return player + grid[index + 1:]
    elif index == 8:
        return grid[:index] + player
    else:
        return grid[:index] + player + grid[index + 1:]


def print_grid(grid):
    print('---------')
    print('|' + ' ' + grid[0] + ' ' + grid[1] + ' ' + grid[2] + ' ' + '|')
    print('|' + ' ' + grid[3] + ' ' + grid[4] + ' ' + grid[5] + ' ' + '|')
    print('|' + ' ' + grid[6] + ' ' + grid[7] + ' ' + grid[8] + ' ' + '|')
    print('---------')


def switch_turn(x):
    if x == "X":
        return "O"
    else:
        return "X"


cells = "         "
turn = "X"
print_grid(cells)

while True:
    print("Enter coords: ")
    row, col = input().split()
    while coords_failed(row, col, cells):
        print("Enter coords: ")
        row, col = input().split()
    cells = make_move(row, col, cells, turn)
    print_grid(cells)
    if check_impossible(cells):
        print("Impossible")
    elif check_win(turn):
        print(f"{turn} wins")
        break
    turn = switch_turn(turn)
    if check_not_finished(cells):
        continue
        #  print("Game not finished")
    else:
        print("Draw")
        break
