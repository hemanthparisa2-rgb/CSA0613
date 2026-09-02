def findKthPositive(arr, k):
    num = 1
    i = 0

    while k > 0:
        if i < len(arr) and arr[i] == num:
            i += 1
        else:
            k -= 1
            if k == 0:
                return num
        num += 1

print(findKthPositive([2,3,4,7,11], 5))
print(findKthPositive([1,2,3,4], 2))
