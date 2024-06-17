def solve_sudoku(board):
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                for n in range(1, 10):
                    if possible(board, y, x, n):
                        board[y][x] = n
                        solve_sudoku(board)
    return board

def possible(b, y, x, n):
    for i in range(0, 9):
        if b[y][i] == n:
            return False
    for i in range(0, 9):
        if b[i][x] == n:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if b[y0 + i][x0 + j] == n:
                return False
    return True