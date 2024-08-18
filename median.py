import math


def findMedianSortedArrays(num1, num2):
    num = num1 + num2
    num.sort()
    if len(num) % 2 != 0:
        return num[len(num) // 2]
    else:
        return (num[len(num) // 2] + num[(len(num) // 2) - 1]) / 2


nums1 = [1, 2]
nums2 = [3, 4]
print(findMedianSortedArrays(nums1, nums2))  # Output: 2.00000
