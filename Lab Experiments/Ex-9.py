arr = [3, 4, 6, -9, 10, 8, 9, 30]
key = 10

arr.sort()   # Sort the array

low = 0
high = len(arr) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        print("Element", key, "is found at position", mid + 1)
        found = True
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Element", key, "is not found")
