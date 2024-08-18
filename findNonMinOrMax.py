def findNonMinOrMax(nums):
    nums = list(set(nums))
    if len(nums) < 3:
        return -1
    nums.sort()
    print(nums)
    return nums[1]


nums = [3, 2, 2, 4]
print(findNonMinOrMax(nums))  # Output: [2, 4]
