def move_ball(board):
    directions = {'E': (0, 1), 'N': (-1, 0), 'W': (0, -1), 'S': (1, 0)}
    corners = {'\\': {'E': 'S', 'N': 'W', 'W': 'N', 'S': 'E'}, '/': {'E': 'N', 'N': 'E', 'W': 'S', 'S': 'W'}}
    rows = len(board)
    cols = len(board[0])
    ball_pos = None
    ball_dir = None
    for i in range(rows):
        for j in range(cols):
            if board[i][j] in directions:
                ball_pos = (i, j)
                ball_dir = board[i][j]
                break
    path = [ball_pos]
    while board[ball_pos[0]][ball_pos[1]] != 'X':
        next_pos = (ball_pos[0] + directions[ball_dir][0], ball_pos[1] + directions[ball_dir][1])
        if board[next_pos[0]][next_pos[1]] in corners:
            ball_dir = corners[board[next_pos[0]][next_pos[1]]][ball_dir]
        ball_pos = next_pos
        path.append(ball_pos)
    return path