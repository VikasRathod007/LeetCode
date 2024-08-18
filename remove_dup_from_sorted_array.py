# import sys


# def removeduplicates(nums):
#     count = 0
#     # for i in range(0, len(nums) - 1):
#     #     if nums[i] == nums[i + 1]:
#     #         nums[i] = sys.maxsize
#     #         count += 1
#     # print(count)
#     # print(nums)
#     # nums.sort()
#     # print(nums)
#     print(len(nums) - len(set(nums)))


# arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# n = len(arr)
# nums = removeduplicates(arr)
S = "GeeksForGeeks"
string = "".join(sorted(S))
print(string)
