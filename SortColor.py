from collections import defaultdict


def sortColors(nums):
    # count = defaultdict(int)
    # for num in nums:
    #     count[num] += 1
    # index = 0
    # for color in range(3):
    #     for _ in range(count[color]):
    #         nums[index] = color
    #         index += 1
    # return nums
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            mid += 1
            low += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums


nums = [2, 0, 2, 1, 1, 0]
print(sortColors(nums))
