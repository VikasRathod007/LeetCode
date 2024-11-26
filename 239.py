# Sliding Window Maximum
from collections import deque


def maxSlidingWindow(nums, k):
    # res = []
    # for i in range(len(nums) - k + 1):
    #     cur_max = max(nums[i : i + k])
    #     res.append(cur_max)
    # return res
    # DeQueue method
    res = []
    deq = deque()
    for i in range(len(nums)):
        if deq and deq[0] < i - k + 1:
            deq.popleft()
        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()
        deq.append(i)
        if i >= k - 1:
            res.append(nums[deq[0]])
    return res


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(maxSlidingWindow(nums, k))
