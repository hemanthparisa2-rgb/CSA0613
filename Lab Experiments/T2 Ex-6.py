def findPeak(nums):
    low, high = 0, len(nums) - 1

    while low < high:
        mid = (low + high) // 2
        if nums[mid] < nums[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return low

print(findPeak([1,2,3,1]))
print(findPeak([1,2,1,3,5,6,4]))
