def champagneTower(poured, query_row, query_glass):
    dp = [[0.0] * 101 for _ in range(101)]
    dp[0][0] = poured

    for i in range(query_row + 1):
        for j in range(i + 1):
            if dp[i][j] > 1:
                extra = (dp[i][j] - 1) / 2
                dp[i + 1][j] += extra
                dp[i + 1][j + 1] += extra
                dp[i][j] = 1

    return min(1, dp[query_row][query_glass])

# Example 1
print("{:.5f}".format(champagneTower(1, 1, 1)))

# Example 2
print("{:.5f}".format(champagneTower(2, 1, 1)))
