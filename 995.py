def minKBitFlips(nums, k):
    c = 0
    for i in range(len(nums) - k + 1):
        if nums[i] == 0:
            for j in range(k):
                nums[i + j] = 1 if nums[i + j] == 0 else 0
            c += 1
    for i in range(len(nums)):
        if nums[i] == 0:
            return -1
    return c


nums = [0, 1, 0]
k = 1
print(minKBitFlips(nums, k))
