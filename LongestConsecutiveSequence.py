def longestConsecutive(nums):
    if not nums:
        return 0
    nums.sort()
    print(nums)
    longest = 1
    current = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            current += 1
            longest = max(current, longest)

        elif nums[i] != nums[i - 1]:
            current = 1
    return longest


nums = [2, 20, 4, 10, 3, 4, 5]
print(longestConsecutive(nums))
