def threeSum(nums):
    i = 0

    arr = set()
    for i in range(len(nums) - 2):
        j = i + 1
        k = len(nums) - 1
        while j < k:
            if nums[i] + nums[j] + nums[k] == 0:
                triplet = (nums[i], nums[j], nums[k])
                print(triplet)
                arr.add(triplet)
                # i += 1
                j += 1
                k -= 1
            elif nums[i] + nums[j] + nums[k] < 0:
                # i += 1
                j += 1
            else:
                k -= 1
    return [list(x) for x in arr]


nums = [-1, 0, 1, 2, -1, -4]

nums.sort()
print(nums)
print(threeSum(nums))  # Output: [[-1, -1, 2], [-1, 0, 1]]
