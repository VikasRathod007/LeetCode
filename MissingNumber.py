# Smallest Positive Missing Number
def missingNumber(nums):
    # this uses O(n) time and O(n) space
    n = len(nums)
    # hash_ = set(nums)
    # i = 1
    # while True:
    #     if i in hash_:
    #         i += 1
    #     else:
    #         return i
    # this uses O(n) time and O(1) space
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1


arr = [2, -3, 4, 1, 1, 7]

print(missingNumber(arr))
