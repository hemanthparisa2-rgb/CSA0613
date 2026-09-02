def climbStairs(n):
    if n <= 2:
        return n

    a, b = 1, 2
    for i in range(3, n + 1):
        a, b = b, a + b
    return b

# Example 1
print(climbStairs(4))

# Example 2
print(climbStairs(3))
