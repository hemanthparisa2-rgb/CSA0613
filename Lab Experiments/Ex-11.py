def findPaths(m, n, N, i, j):
    dp = [[0] * n for _ in range(m)]
    dp[i][j] = 1
    ans = 0

    for step in range(N):
        temp = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if dp[r][c]:
                    for x, y in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nr, nc = r + x, c + y
                        if 0 <= nr < m and 0 <= nc < n:
                            temp[nr][nc] += dp[r][c]
                        else:
                            ans += dp[r][c]
        dp = temp

    return ans

print(findPaths(2, 2, 2, 0, 0))
