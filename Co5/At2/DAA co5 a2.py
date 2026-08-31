def max_cut(graph):
    n = len(graph)
    group = [-1] * n
    best_group = []
    best_cut = 0

    def cut_value():
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if graph[i][j] and group[i] != group[j]:
                    count += 1
        return count

    def backtrack(v):
        nonlocal best_cut, best_group

        if v == n:
            current = cut_value()
            if current > best_cut:
                best_cut = current
                best_group = group[:]
            return

        for side in [0, 1]:
            group[v] = side

            # Pruning
            current = cut_value()
            if current >= best_cut:
                backtrack(v + 1)

            group[v] = -1

    backtrack(0)
    return best_group, best_cut


# Input graph (Adjacency Matrix)
graph = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]

partition, max_edges = max_cut(graph)

A = [i + 1 for i in range(len(partition)) if partition[i] == 0]
B = [i + 1 for i in range(len(partition)) if partition[i] == 1]

print("Maximum Cut Problem")
print("Group A:", A)
print("Group B:", B)
print("Maximum Cut Edges:", max_edges)
