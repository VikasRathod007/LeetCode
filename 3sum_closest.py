# 16. 3Sum Closest
import sys
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        x = sys.maxsize
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                Sum = nums[i] + nums[l] + nums[r]
                if Sum == target:
                    return Sum
                if abs(Sum - target) < abs(x - target):
                    x = Sum
                elif Sum > target:
                    r -= 1
                else:
                    l += 1
        return x


nums = [-1, 2, 1, -4]
target = 1
print(Solution().threeSumClosest(nums, target))  # Output: 2
