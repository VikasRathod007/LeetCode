# 153. Find Minimum in Rotated Sorted Array
def findMin(nums):
    low, high = 0, len(nums) - 1
    min_ = 0
    while low < high:
        mid = (low + high) // 2
        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid
    return nums[low]


nums = [3, 4, 5, 6, 1, 2]
print(findMin(nums))
