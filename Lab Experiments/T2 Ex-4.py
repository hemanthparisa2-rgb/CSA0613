def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

# Test Case 1
print(insertion_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]))

# Test Case 2
print(insertion_sort([5, 5, 5, 5, 5]))

# Test Case 3
print(insertion_sort([2, 3, 1, 3, 2, 1, 1, 3]))
