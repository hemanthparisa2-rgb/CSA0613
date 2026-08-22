s = input("Enter string: ")
n = len(s)
if n == 0:
    print("Input string is empty")
    print("Length = 0")
else:
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1

    # Build DP table
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if s[i] == s[j]:
                if length == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    i = 0
    j = n - 1
    left = []
    right = []

    while i <= j:
        if i == j:
            left.append(s[i])
            break
        if s[i] == s[j]:
            left.append(s[i])
            right.append(s[j])
            i += 1
            j -= 1

        elif dp[i + 1][j] >= dp[i][j - 1]:
            i += 1
        else:
            j -= 1
    palindrome = ''.join(left) + ''.join(right[::-1])
    print("\n===== LONGEST PALINDROMIC SUBSEQUENCE =====")
    print("Longest Palindromic Subsequence:", palindrome)
    print("Length =", dp[0][n - 1])
