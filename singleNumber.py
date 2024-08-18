from collections import Counter


def singleNumber(nums):
    if len(nums) == 1:
        return nums[0]

    num = Counter(nums)
    for key, val in num.items():
        if val == 1:
            return key


nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))
