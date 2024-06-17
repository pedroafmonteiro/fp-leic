def magic(mat):
    n = len(mat)
    target_sum = sum(mat[0])
    
    # Check rows
    for row in mat:
        if sum(row) != target_sum:
            return False
    
    # Check columns
    for j in range(n):
        col_sum = 0
        for i in range(n):
            col_sum += mat[i][j]
        if col_sum != target_sum:
            return False
    
    # Check diagonal from top-left to bottom-right
    diag_sum = 0
    for i in range(n):
        diag_sum += mat[i][i]
    if diag_sum != target_sum:
        return False
    
    # Check diagonal from top-right to bottom-left
    diag_sum = 0
    for i in range(n):
        diag_sum += mat[i][n-i-1]
    if diag_sum != target_sum:
        return False
    
    # If all checks passed, it's a magic square
    return True
