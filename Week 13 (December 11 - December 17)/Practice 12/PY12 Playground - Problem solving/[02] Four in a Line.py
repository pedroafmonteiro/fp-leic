def four_in_line(board):
    if winner_horizontal(board) is not None:
        return winner_horizontal(board)
    elif winner_vertical(board) is not None:
        return winner_vertical(board)
    elif winner_diagonal1(board) is not None:
        return winner_diagonal1(board)
    elif winner_diagonal2(board) is not None:
        return winner_diagonal2(board)
    else:
        return {}

def winner_horizontal(b):
    for row in range(0, len(b)):
        for col in range(0, len(b[row]) - 3):
            if b[row][col] == 0:
                continue
            if b[row][col] == b[row][col + 1] and b[row][col] == b[row][col + 2] and b[row][col] == b[row][col + 3]:
                return {(row, col), (row, col + 3)}

def winner_vertical(b):
    for row in range(0, len(b) - 3):
        for col in range(0, len(b[row])):
            if b[row][col] == 0:
                continue
            if b[row][col] == b[row + 1][col] and b[row][col] == b[row + 2][col] and b[row][col] == b[row + 3][col]:
                return {(row, col), (row + 3, col)}

def winner_diagonal1(b):
    for row in range(0, len(b) - 3):
        for col in range(0, len(b[row]) - 3):
            if b[row][col] == 0:
                continue
            if b[row][col] == b[row + 1][col + 1] and b[row][col] == b[row + 2][col + 2] and b[row][col] == b[row + 3][col + 3]:
                return {(row, col), (row + 3, col + 3)}

def winner_diagonal2(b):
    for row in range(0, len(b) - 3):
        for col in range(3, len(b[row])):
            if b[row][col] == 0:
                continue
            if b[row][col] == b[row + 1][col - 1] and b[row][col] == b[row + 2][col - 2] and b[row][col] == b[row + 3][col - 3]:
                return {(row, col), (row + 3, col - 3)}