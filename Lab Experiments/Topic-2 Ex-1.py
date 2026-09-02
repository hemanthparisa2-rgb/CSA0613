def sort_list(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# Test Cases
print(sort_list([]))
print(sort_list([1]))
print(sort_list([7, 7, 7, 7]))
print(sort_list([-5, -1, -3, -2, -4]))
