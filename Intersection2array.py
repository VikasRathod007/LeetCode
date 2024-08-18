# def intersect(nums1, nums2):
#     num1 = set(nums1)
#     num2 = set(nums2)
#     print(num1)
#     print(num2)
#     res = list(num1 & num2)
#     # for i in num2:
#     #     if i in num1:
#     #         res.append(i)
#     return res
from collections import Counter


def intesect2(nums1, nums2):
    counts = Counter(nums1)
    res = []
    for i in nums2:
        if counts[i] > 0:
            res.append(i)
            counts[i] -= 1
    return res


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intesect2(nums1, nums2))
