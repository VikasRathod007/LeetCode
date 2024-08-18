def numberOfSubarrays(nums, k):
    num = [0 if num % 2 == 0 else 1 for num in nums]
    print(num)
    prefix_sum = 0
    count = {0: 1}
    nice_subarray = 0
    for i in num:
        prefix_sum += i
        if prefix_sum - k in count:
            nice_subarray += count[prefix_sum - k]
        if prefix_sum in count:
            count[prefix_sum] += 1
        else:
            count[prefix_sum] = 1
    return nice_subarray


nums = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]

k = 2
print(numberOfSubarrays(nums, k))
