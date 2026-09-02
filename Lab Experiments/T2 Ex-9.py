from math import sqrt

points = [(1,2), (4,5), (7,8), (3,1)]

min_dist = float('inf')
pair = ()

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        d = sqrt((points[i][0]-points[j][0])**2 +
                 (points[i][1]-points[j][1])**2)

        if d < min_dist:
            min_dist = d
            pair = (points[i], points[j])

print("Closest pair:", pair)
print("Minimum distance:", min_dist)
