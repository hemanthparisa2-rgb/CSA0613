import random
import time
import sys
sys.setrecursionlimit(5000)

current_depth = 0
max_depth = 0


def merge(arr, left, mid, right):
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    i = 0
    j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):
    global current_depth, max_depth

    current_depth += 1

    if current_depth > max_depth:
        max_depth = current_depth

    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        merge(arr, left, mid, right)

    current_depth -= 1

n = int(input("Enter number of elements: "))

arr = [random.randint(1, 100000) for _ in range(n)]

start = time.perf_counter()

merge_sort(arr, 0, len(arr)-1)

end = time.perf_counter()

print("\nMerge Sort Completed Successfully")
print("Execution Time :", end - start, "seconds")
print("Maximum Recursion Stack Depth :", max_depth)
frame_size = sys.getsizeof(sys._getframe())
stack_memory = frame_size * max_depth

print("Approximate Stack Memory :", stack_memory, "bytes")
