from itertools import combinations

def knapsack(weights, values, capacity):
    n = len(weights)
    best_value = 0
    best_items = []

    for r in range(n+1):
        for comb in combinations(range(n), r):
            w = sum(weights[i] for i in comb)
            v = sum(values[i] for i in comb)

            if w <= capacity and v > best_value:
                best_value = v
                best_items = list(comb)

    return best_items, best_value

weights = [2,3,1]
values = [4,5,3]
capacity = 4

items, value = knapsack(weights, values, capacity)

print(items)
print(value)
