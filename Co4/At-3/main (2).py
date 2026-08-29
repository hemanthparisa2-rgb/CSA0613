
n = int(input("Enter number of items: "))
weights = list(map(int, input("Enter weights: ").split()))
values = list(map(int, input("Enter values: ").split()))
capacity = int(input("Enter capacity: "))

# 0/1 Knapsack - Dynamic Programming
dp = [[0] * (capacity + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for w in range(capacity + 1):
        if weights[i-1] <= w:
            dp[i][w] = max(dp[i-1][w],
                            values[i-1] + dp[i-1][w-weights[i-1]])
        else:
            dp[i][w] = dp[i-1][w]

w = capacity
knapsack = []

for i in range(n, 0, -1):
    if dp[i][w] != dp[i-1][w]:
        knapsack.append(i)
        w -= weights[i-1]

knapsack.reverse()

# Greedy Container Loading
items = sorted(range(n), key=lambda i: weights[i])
remaining = capacity
greedy = []

for i in items:
    if weights[i] <= remaining:
        greedy.append(i + 1)
        remaining -= weights[i]

dp_weight = sum(weights[i-1] for i in knapsack)
greedy_weight = sum(weights[i-1] for i in greedy)

print("\n0/1 Knapsack (DP)")
print("Selected Items:", knapsack)
print("Total Weight:", dp_weight)
print("Total Value:", dp[ n ][capacity])
print("Utilization:", round(dp_weight / capacity * 100, 2), "%")

print("\nContainer Loading (Greedy)")
print("Selected Items:", greedy)
print("Total Weight:", greedy_weight)
print("Utilization:", round(greedy_weight / capacity * 100, 2), "%")

