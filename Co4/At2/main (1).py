import heapq
n = int(input("Enter number of locations: "))
r = int(input("Enter number of roads: "))
graph = [[] for _ in range(n)]
print("Enter: From To Distance TrafficFactor")
for _ in range(r):
    u, v, d, t = map(int, input().split())
    cost = d * t
    graph[u].append((v, cost))
    graph[v].append((u, cost))
start = int(input("Enter collection center: "))
end = int(input("Enter disposal point: "))
dist = [float('inf')] * n
parent = [-1] * n
dist[start] = 0
pq = [(0, start)]
while pq:
    d, u = heapq.heappop(pq)
    if d > dist[u]:
        continue
    for v, cost in graph[u]:
        if d + cost < dist[v]:
            dist[v] = d + cost
            parent[v] = u
            heapq.heappush(pq, (dist[v], v))
path = []
v = end
while v != -1:
    path.append(v)
    v = parent[v]
path.reverse()
fuel = dist[end] * 0.08
fuel_cost = fuel * 100
print("\nOptimal Route:", " -> ".join(map(str, path)))
print("Total Travel Cost:", dist[end], "units")
print("Estimated Fuel:", round(fuel, 2), "litres")
print("Estimated Fuel Cost: Rs.", round(fuel_cost, 2))
print("Vehicle Capacity: 1000 kg")
print("CO2 emissions are reduced by using shorter routes.")
