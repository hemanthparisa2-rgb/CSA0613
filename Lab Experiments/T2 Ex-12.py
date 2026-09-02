from itertools import permutations
from math import sqrt

def distance(a, b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def tsp(cities):
    start = cities[0]
    best = float('inf')
    path = None

    for p in permutations(cities[1:]):
        tour = [start] + list(p) + [start]
        dist = 0

        for i in range(len(tour)-1):
            dist += distance(tour[i], tour[i+1])

        if dist < best:
            best = dist
            path = tour

    return best, path

cities = [(1,2),(4,5),(7,1),(3,6)]

d, p = tsp(cities)
print(d)
print(p)
