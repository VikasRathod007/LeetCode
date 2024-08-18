def searchRange(nums, target):
    res = []
    if not nums:
        return [-1, -1]

    # for i in range(0, len(nums)):
    #     if nums[i] == target:
    #         res.append(i)
    #     elif nums[i] > target:
    #         break
    # if not res:
    #     return [-1, -1]
    # return res
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            first = mid
            last = mid
            while first > 0 and nums[first - 1] == target:
                first -= 1
            while last + 1 < len(nums) and nums[last + 1] == target:
                last += 1
            return [first, last]
    return [-1, -1]


nums = [5, 7, 7, 8, 8, 9]
target = 5
print(searchRange(nums, target))
