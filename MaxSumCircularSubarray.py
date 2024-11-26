def maxSubarraySumCircular(nums):
    curr_min, curr_max = 0, 0
    global_min, global_max = nums[0], nums[0]
    total_ = 0

    for i in range(len(nums)):
        total_ += nums[i]
        curr_max = max(nums[i], curr_max + nums[i])
        global_max = max(global_max, curr_max)
        curr_min = min(nums[i], curr_min + nums[i])
        global_min = min(global_min, curr_min)

    return max(global_max, total_ - global_min) if global_max > 0 else global_max


nums = [5, -3, 5]

print(maxSubarraySumCircular(nums))
