def canJump(nums):
    goal = len(nums) - 1
    for i in range(goal - 1, -1, -1):
        if i + nums[i] >= goal:
            print(i + nums[i])
            goal = i
    return True if goal == 0 else False


nums = [2, 3, 1, 1, 4]
print(canJump(nums))
