def mult(M, N):
    if len(M[0]) != len(N):
        return []
    result = [[0 for _ in range(len(N[0]))] for _ in range(len(M))]
    for i in range(len(M)):
        for j in range(len(N[0])):
            for k in range(len(N)):
                result[i][j] += M[i][k] * N[k][j]
    return result