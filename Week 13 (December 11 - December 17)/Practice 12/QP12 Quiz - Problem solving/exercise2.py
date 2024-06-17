def tic_tac_toe(board, player):
  board = [list(row) for row in board.split('\n') if row.strip()]
  patterns = [
    [(0, 0), (0, 1), (0, 2)],  
    [(1, 0), (1, 1), (1, 2)],  
    [(2, 0), (2, 1), (2, 2)],  
    [(0, 0), (1, 0), (2, 0)],  
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)] 
  ]
  for i in range(3):
    for j in range(3):
      if board[i][j] == ' ':
        board[i][j] = player
        for pattern in patterns:
          if all(board[x][y] == player for x, y in pattern):
            return chr(ord('A') + i) + str(j + 1)
        board[i][j] = ' '
  return None