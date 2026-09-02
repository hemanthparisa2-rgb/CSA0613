def find_min_max(arr):
    minimum = maximum = arr[0]

    for x in arr:
        if x < minimum:
            minimum = x
        if x > maximum:
            maximum = x

    return minimum, maximum


# Test Case 1
arr = [5, 7, 3, 4, 9, 12, 6, 2]
print("Min =", find_min_max(arr)[0], "Max =", find_min_max(arr)[1])

# Test Case 2
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
print("Min =", find_min_max(arr)[0], "Max =", find_min_max(arr)[1])

# Test Case 3
arr = [22, 34, 35, 36, 43, 67, 12, 13, 15, 17]
print("Min =", find_min_max(arr)[0], "Max =", find_min_max(arr)[1])