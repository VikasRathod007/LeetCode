def thirdMax(nums):
    nums = list(set(nums))
    if len(nums) < 3:
        return max(nums)

    nums.sort(reverse=True)
    return nums[2]


nums = [1, 1, 2]
print(thirdMax(nums))  # Output: 1
print(len(nums))
