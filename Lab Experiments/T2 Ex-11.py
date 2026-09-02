def convexHull(points):
    hull = []

    for i in range(len(points)):
        for j in range(i+1, len(points)):
            left = right = 0

            for k in range(len(points)):
                if k == i or k == j:
                    continue

                val = ((points[j][0]-points[i][0])*(points[k][1]-points[i][1]) -
                       (points[j][1]-points[i][1])*(points[k][0]-points[i][0]))

                if val > 0:
                    left += 1
                elif val < 0:
                    right += 1

            if left == 0 or right == 0:
                if points[i] not in hull:
                    hull.append(points[i])
                if points[j] not in hull:
                    hull.append(points[j])

    return hull

points = [(1,1),(4,6),(8,1),(0,0),(3,3)]
print(convexHull(points))
