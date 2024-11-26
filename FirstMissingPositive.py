# Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.


def firstMissingPositive(nums):
    # uses 0(n) time and 0(n) space
    n = len(nums)
    hash_ = set(nums)
    i = 1
    while True:
        if i in hash_:
            i += 1
        else:
            return i


nums = [1, 2, 3, 4]
print(firstMissingPositive(nums))
