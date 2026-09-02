from itertools import permutations

def assignment_problem(cost):
    n = len(cost)
    best = float('inf')
    assign = None

    for p in permutations(range(n)):
        total = 0
        for i in range(n):
            total += cost[i][p[i]]

        if total < best:
            best = total
            assign = p

    return assign, best

cost = [[3,10,7],
        [8,5,12],
        [4,6,9]]

a, c = assignment_problem(cost)

print("Assignment:", a)
print("Cost:", c)
