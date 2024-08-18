def subsets(nums):
    arr = [[]]
    print(arr)
    for i in range(1, len(nums)):
        for j in range(i + 1, len(nums)):
            print(i, j)


nums = [1, 2, 3]
print(subsets(nums))
