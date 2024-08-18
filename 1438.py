from sortedcontainers import SortedList


def longestSubarray(nums, limit):
    sorted_list = SortedList()
    left = 0
    max_lenght = 0
    for right in range(len(nums)):
        sorted_list.add(nums[right])
        while sorted_list[-1] - sorted_list[0] > limit:
            sorted_list.remove(nums[left])
            left += 1
        max_lenght = max(max_lenght, right - left + 1)
    return max_lenght


nums = [8, 2, 4, 7]
limit = 4
print(longestSubarray(nums, limit))
