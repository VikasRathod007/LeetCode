# 974. Subarray Sums Divisible by K
def subarraysDivByK(num, k):
    count = 0
    for i in range(len(num)):
        for j in range(i, len(num)):
            if sum(num[i : j + 1]) % k == 0:
                count += 1
    return count


nums = [4, 5, 0, -2, -3, 1]
k = 5
print(subarraysDivByK(nums, k))
