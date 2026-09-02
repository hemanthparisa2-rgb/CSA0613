def rob(nums):
    if len(nums) == 1:
        return nums[0]

    def helper(arr):
        prev = curr = 0
        for x in arr:
            prev, curr = curr, max(curr, prev + x)
        return curr

    return max(helper(nums[:-1]), helper(nums[1:]))

# Example 1
nums = [2, 3, 2]
print(rob(nums))

# Example 2
nums = [1, 2, 3, 1]
print(rob(nums))
