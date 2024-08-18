def minIncrementForUnique(nums):
    nums.sort()
    res = 0
    inc = 0
    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            inc = nums[i - 1] + 1 - nums[i]
            res += inc
            nums[i] = nums[i - 1] + 1
    return res


nums = [3, 2, 1, 2, 1, 7]
print(minIncrementForUnique(nums))
