def gameOfLife(board):
    m = len(board)
    n = len(board[0])

    dirs = [(-1,-1),(-1,0),(-1,1),
            (0,-1),(0,1),
            (1,-1),(1,0),(1,1)]

    new = [[0]*n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            live = 0
            for x, y in dirs:
                r, c = i+x, j+y
                if 0 <= r < m and 0 <= c < n:
                    live += board[r][c]

            if board[i][j] == 1 and (live == 2 or live == 3):
                new[i][j] = 1
            elif board[i][j] == 0 and live == 3:
                new[i][j] = 1

    return new

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
print(gameOfLife(board))
