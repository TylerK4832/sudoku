def check9(board):
    for row in board:
        temprow = sorted(row)
        for i in range(9):
            if int(temprow[i]) != i+1:
                print("No")
                return -1

def sudoku():
    board = []

    for i in range(9):
        t = str(input("Enter row: "))
        y = list(t)
        if len(y) != 9  or t.isdigit() == False:
            print("Invalid input")
            return -1
        board.append(y)

    if check9(board) == -1:
        return(-1)

    tempboard = []
    for i in range(9):
        col = []
        for q in range(9):
            col.append(board[q][i])
        tempboard.append(col)
    if check9(tempboard) == -1:
        return(-1)

    tempboard = []
    for y in range(3):
        for x in range(3):
            box = []
            for y2 in range(3):
                for x2 in range(3):
                    box.append(board[(3*y)+y2][(3*x)+x2])
            tempboard.append(box)
    if check9(tempboard) == -1:
        return(-1)

    print("Yes")

sudoku()

input("Press enter to close")
