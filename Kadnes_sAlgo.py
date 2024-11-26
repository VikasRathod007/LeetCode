def maxSubArraySum(arr):
    n = len(arr)
    max_sum = float("-inf")
    curr_sum = 0
    res = []
    for i in range(n):
        curr_sum += arr[i]
        max_sum = max(max_sum, curr_sum)
        res.append(curr_sum)
        if curr_sum < 0:
            curr_sum = 0
    return max_sum, res


arr = [2, 3, -8, 7, -1, 2, 3]
print(maxSubArraySum(arr))
