def minOperations(nums):
    c = 0
    for i in range(len(nums) - 2):
        if nums[i] == 0:
            for j in range(0, 3):
                nums[i + j] = 1 if nums[i + j] == 0 else 0
            c += 1
    for i in range(len(nums)):
        if nums[i] == 0:
            return -1
    return c


nums = [0, 1, 1, 1, 0, 0]
print(minOperations(nums))
