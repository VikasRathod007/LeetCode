def numberOfPairs(nums1, nums2, k):
    count = 0
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] % (nums2[j] * k) == 0:
                print(nums1[i], nums2[j], i, j)
                count += 1
    return count


nums1 = [1, 3, 4]
nums2 = [1, 3, 4]
k = 1
print(numberOfPairs(nums1, nums2, k))  # Output: 2
# print(nums1[0] // (nums2[1] * k))
