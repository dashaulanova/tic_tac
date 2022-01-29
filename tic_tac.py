def board_output(*arg):
    for i in arg:
        print(*i)
    return


def make_move(a, *b):
    x, y = input("Ходит игрок " + a + ", введите координаты клетки через пробел (<строка> <столбец>):").split()
    x = int(x) + 1
    y = int(y) + 1
    b[x][y] = a
    board_output(*b)
    return


def victory_check(arg, *t):
    if any(
            [t[1][1] == t[2][1] == t[3][1] != "-",
             t[1][2] == t[2][2] == t[3][2] != "-",
             t[1][3] == t[2][3] == t[3][3] != "-",
             t[1][1] == t[1][2] == t[1][3] != "-",
             t[2][1] == t[2][2] == t[2][3] != "-",
             t[3][1] == t[3][2] == t[3][3] != "-",
             t[1][1] == t[2][2] == t[3][3] != "-",
             t[3][1] == t[2][2] == t[1][3] != "-"]):
        print("Ура! Победил игрок ", arg)
        global check_break
        check_break = 0
        return


check_break, counter = 1, 9
board = [[" ", "0", "1", "2"],
         ["0", "-", "-", "-"],
         ["1", "-", "-", "-"],
         ["2", "-", "-", "-"]]
print("Начинаем игру!")
board_output(*board)
while True:
    if counter % 2 == 1:
        player = "0"
    else:
        player = "x"
    make_move(player, *board)
    victory_check(player, *board)
    if check_break == 0:
        break
    counter -= 1
    if counter == 0:
        print("Ничья!")
        break
