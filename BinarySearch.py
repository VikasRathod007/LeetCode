def search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


nums = [-1, 0, 2, 4, 6, 8]
target = 4
print(search(nums, target))  # Output: 3
# mid = len(nums) // 2
# print(mid)
